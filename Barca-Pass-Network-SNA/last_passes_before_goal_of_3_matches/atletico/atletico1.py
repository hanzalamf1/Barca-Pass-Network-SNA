import networkx as nx
import matplotlib.pyplot as plt

# Ağ oluşturma
G = nx.DiGraph()

# Düğümler ve bağlantılar
edges = [
    ("Nélson Cabral Semedo", "Marc-André ter Stegen"),
    ("Marc-André ter Stegen", "Rafael Alcântara do Nascimento"),
    ("Rafael Alcântara do Nascimento", "Jordi Alba Ramos"),
    ("Jordi Alba Ramos", "Lionel Andrés Messi Cuccittini"),
    ("Lionel Andrés Messi Cuccittini", "Ousmane Dembélé"),
    ("Ousmane Dembélé", "Goal"),
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
