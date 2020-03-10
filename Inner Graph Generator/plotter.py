import networkx as nx
import matplotlib.pyplot as plt
g=nx.Graph()
# g.add_edges_from([(0, 1), (1, 2), (1, 3), (2, 4), (2, 3), (2, 5), (3, 4), (3, 6), (4, 5), (4, 6), (5, 6), (5, 7), (6, 7), (7, 8)])

g.add_edges_from([(0, 1), (1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5), (5, 6)])
# g.add_edges_from([(0, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5)]) #wrapped vertex attached
# plt.subplots(21)
nx.draw(g, labels=None, node_size=900, node_color='#87ceeb', font_weight='bold')
plt.show()
print(g.edges)
