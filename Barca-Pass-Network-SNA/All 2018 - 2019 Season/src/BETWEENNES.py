import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Excel dosyasındaki veriyi okuma
file_path = "C:/Users/hanza/Desktop/merged/finished.xlsx"
df = pd.read_excel(file_path)

# Sütun isimlerini kontrol etme
print(df.columns)

# Sütun adlarındaki ekstra boşlukları temizleme (varsa)
df.columns = df.columns.str.strip()

# Güncellenmiş oyuncu konumları (4-3-3 formasyonu)
player_positions = {
    'Marc-André ter Stegen': (0, 5),    # Kaleci
    'Sergi Roberto Carnicer': (1, 2),   # Sol Defans (kenara açıldı)
    'Jordi Alba Ramos': (1, 8),   # Sağ Defans (kenara açıldı)
    'Gerard Piqué Bernabéu': (0.7, 4),   # Defans 1 (kaleye daha yakın)
    'Clément Lenglet': (0.7, 6),   # Defans 2 (kaleye daha yakın)
    'Arthur Henrique Ramos de Oliveira Melo': (2.5, 3),   # Orta Saha 1
    'Ivan Rakitić': (2.1, 5),   # Orta Saha 2
    'Arturo Erasmo Vidal Pardo': (2.5, 7),   # Orta Saha 3
    'Lionel Andrés Messi Cuccittini': (3.5, 2),    # Sol Forvet
    'Luis Alberto Suárez Díaz': (4, 5),    # Santrafor
    'Ousmane Dembélé': (3.5, 8),    # Sağ Forvet

    # YEDEKLER
    'Sergio Busquets i Burgos': (1.9, 4.5),   # Orta Saha 1
    'Carles Aleña Castillo': (2.3, 2.5),   # YEDEK Orta Saha
    'Nélson Cabral Semedo': (1.2, 7.5),   # YEDEK Defans
    'Philippe Coutinho Correia': (3.3, 7.5),    # YEDEK Orta Saha
    'Samuel Yves Umtiti': (0.9, 3.5),    # YEDEK Defans
    'Thomas Vermaelen': (0.9, 5.5),   # YEDEK Defans
    'Malcom Filipe Silva de Oliveira': (3.5, 5.5),   # YEDEK Forvet
}
# Pas ağına oyuncuları ekle
G = nx.DiGraph()  # Directed graph (yönlü grafik)
# 11 oyuncu için node'lar ekle
for player in player_positions:
    G.add_node(player, pos=player_positions[player])

# Veriden pasları ekleyerek ağ oluştur
for _, row in df.iterrows():
    player1 = row['player.name']
    player2 = row['pass.recipient.name']
    pass_count = row['Pass Count']
    
    # Bağlantıyı ekle (oyuncular arasındaki pas sayısını ağırlık olarak ekliyoruz)
    G.add_edge(player1, player2, weight=pass_count)

# Degree hesaplama (tüm bağlantıların sayısı)
degrees = G.degree()

# Degree centralization hesaplama
max_degree = max(dict(degrees).values())
total_nodes = len(G.nodes())
centralization = sum(max_degree - degree for _, degree in degrees) / ((total_nodes - 1) * (total_nodes - 2))

# Sonuçları yazdır
print(f"Degree Centralization: {centralization:.4f}")

# Betweenness centrality hesaplama
betweenness_centrality = nx.betweenness_centrality(G)

# Betweenness centrality değerlerini listeye çevirme
betweenness_values = list(betweenness_centrality.values())

# Renk skalası için normalizasyon
norm = plt.Normalize(vmin=min(betweenness_values), vmax=max(betweenness_values))

# Grafik düzenini ayarla
pos = {player: player_positions[player] for player in G.nodes()}

# Grafik boyutunu ayarlama
plt.figure(figsize=(14, 10))

# Betweenness centrality değerlerine göre renk haritası
betweenness_color_map = plt.cm.Greens(norm(betweenness_values))

# Ağı çizme
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=800,  # Düğüm boyutu
    node_color=betweenness_color_map,  # Renk haritası
    font_size=8,  # Yazı tipi boyutu
    font_weight="bold",  # Yazı kalınlığı
    edge_color="gray",  # Kenar rengi
    arrowsize=10,  # Ok büyüklüğü
)

# Kenar etiketlerini (pas sayısını) ekleme
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=6,  # Etiket boyutu
)

# Betweenness centrality renk skalasını ekleyelim
ax = plt.gca()  
plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.Greens, norm=norm), ax=ax, label="Betweenness Centrality")

# Başlık ekle
plt.title("4-3-3 Pas Ağı ve Betweenness Merkeziği", fontsize=16)
plt.show()

