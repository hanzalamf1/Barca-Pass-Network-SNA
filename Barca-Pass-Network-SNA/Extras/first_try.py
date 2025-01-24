import networkx as nx
import matplotlib.pyplot as plt

# Güncellenmiş oyuncu konumları (4-3-3 formasyonu)
player_positions = {
    'Marc-André ter Stegen': (0, 5),    # Kaleci
    'Sergi Roberto Carnicer': (1, 2),   # Sol Defans (kenara açıldı)
    'Jordi Alba Ramos': (1, 8),   # Sağ Defans (kenara açıldı)
    'Gerard Piqué Bernabéu': (0.7, 4),   # Defans 1 (kaleye daha yakın)
    'Clément Lenglet': (0.7, 6),   # Defans 2 (kaleye daha yakın)
    'Arthur Henrique Ramos de Oliveira Melo': (2.5, 3),   # Orta Saha 1
    'Sergio Busquets i Burgos': (2.7, 3.5),   # Orta Saha 1
    'Ivan Rakitić': (2.1, 5),   # Orta Saha 2
    'Arturo Erasmo Vidal Pardo': (2.5, 7),   # Orta Saha 3
    'Carles Aleña Castillo': (2.7, 7.5),   # Orta Saha 3
    'Lionel Andrés Messi Cuccittini': (3.5, 2),    # Sol Forvet
    'Luis Alberto Suárez Díaz': (4, 5),    # Santrafor
    'Ousmane Dembélé': (3.5, 8),    # Sağ Forvet
    'Philippe Coutinho Correia': (3.7, 8.5),    # Sağ Forvet
}

# Pas ağına oyuncuları ekle
G = nx.Graph()

# 11 oyuncu için node'lar ekle
for player in player_positions:
    G.add_node(player, pos=player_positions[player])

# Pas ağı bağlantıları (Mesafeye göre bağlantı ekle)
for player1 in player_positions:
    for player2 in player_positions:
        if player1 != player2:
            x1, y1 = player_positions[player1]
            x2, y2 = player_positions[player2]
            distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            # Mesafe eşiği (yakın oyuncular arasında pas bağlantısı kur)
            if distance < 3:  # Mesafeyi 3 birimden küçük yapalım
                G.add_edge(player1, player2, weight=distance)

# Pas ağını çizme
plt.figure(figsize=(8, 6))

# Grafik düzenini ayarla
pos = {player: player_positions[player] for player in G.nodes()}
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=2000, font_size=10)

# Başlık ekle
plt.title("4-3-3 Pas Ağı (Güncellenmiş Konumlar)")
plt.show()
