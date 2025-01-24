import networkx as nx
import matplotlib.pyplot as plt

# Ağ oluşturma
G = nx.DiGraph()

# Düğümler ve bağlantılar
edges = [
    ("Ivan Rakitić", "Goal"),
    ("Sergi Roberto Carnicer", "Ivan Rakitić"),
    ("Ivan Rakitić", "Sergi Roberto Carnicer"),
    ("Lionel Andrés Messi Cuccittini", "Ivan Rakitić"),
    ("Sergio Busquets i Burgos", "Lionel Andrés Messi Cuccittini"),
    ("Jordi Alba Ramos", "Sergio Busquets i Burgos"),
    ("Arthur Henrique Ramos de Oliveira Melo", "Jordi Alba Ramos"),
    ("Jordi Alba Ramos", "Arthur Henrique Ramos de Oliveira Melo"),
]

G.add_edges_from(edges)

# Düğüm boyutları ve renkleri
node_sizes = [5000 if node == "Goal" else 2000 for node in G.nodes()]
node_colors = ["red" if node == "Goal" else "skyblue" for node in G.nodes()]

# Görselleştirme
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=node_sizes,
    node_color=node_colors,
    font_size=10,
    font_weight="bold",
)
nx.draw_networkx_edges(G, pos, edge_color="black", arrowsize=20)

plt.title("Pas Ağı Analizi")
plt.show()
