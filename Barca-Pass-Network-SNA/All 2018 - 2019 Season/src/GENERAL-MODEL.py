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

# Yönlendirilmiş pas ağına oyuncuları ekle
G = nx.DiGraph()  # DiGraph kullanıyoruz, böylece yönlendirilmiş kenarlar olacak

# 11 oyuncu için node'lar ekle
for player in player_positions:
    G.add_node(player, pos=player_positions[player])

# Veriden pasları ekleyerek ağ oluştur
for _, row in df.iterrows():
    player1 = row['player.name']
    player2 = row['pass.recipient.name']
    pass_count = row['Pass Count']  # Bu sütun ismini kontrol ettik
    
    # Bağlantıyı ekle (oyuncular arasındaki pas sayısını ağırlık olarak ekliyoruz)
    G.add_edge(player1, player2, weight=pass_count)

# Pas ağına oyuncular ve pas sayıları ile bağlantılar ekledik.

# Ağın görselleştirilmesi
plt.figure(figsize=(10, 8))

# Grafik düzenini ayarla
pos = {player: player_positions[player] for player in G.nodes()}
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=2000, font_size=10, font_color='black', arrowsize=20)

# Bağlantılarda pas sayısını göstermek için etiket ekle
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Ağ yoğunluğu
density = nx.density(G)

# Ağ merkezileşmesi
centrality = nx.degree_centrality(G)
centralization = (max(centrality.values()) - sum(centrality.values()) / len(centrality)) / (1 - 1 / len(centrality))

# Ağ bağlantısı
connectivity = nx.node_connectivity(G)

# Güçlü bağlantılı bileşenlerin hesaplanması
scc = list(nx.strongly_connected_components(G))
number_of_scc = len(scc)

# Hesaplamaları sağ alt köşeye ekle
plt.figtext(0.95, 0.05, f"Density: {density:.3f}\nCentralization: {centralization:.3f}\nConnectivity: {connectivity}\nSCC Count: {number_of_scc}", ha="right", fontsize=10)

# Başlık ekle
plt.title("4-3-3 Pas Ağı (Pas Sayılarıyla) - Yönlendirilmiş")

plt.show()

# Güçlü bağlantılı bileşenleri konsola yazdır
print(f"Güçlü bağlantılı bileşenler: {scc}")
