import networkx as nx

# Создаем линейный граф (цепочку из 32 узлов)
G = nx.path_graph(32)

# связываем узлы 14-15-16-17 между собой
G.add_edges_from([(14, 16), (15, 17), (14, 17)])

# Добавляем по две связи на концах
G.add_edges_from([(0, 2), (1, 3), (30, 28), (31, 29)])

# Вычисляем eigenvector centrality
centrality = nx.eigenvector_centrality(G, max_iter=1000)

# Сортируем по номерам узлов
nodes = sorted(centrality.keys())

print(centrality)