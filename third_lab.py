import networkx as nx

# Заданные параметры
n = 70  # количество вершин
p = 0.45  # вероятность появления ребра

# Генерация графа
G = nx.erdos_renyi_graph(n, p)

# Вычисление средней степени вершины в сгенерированном графе
average_degree = sum(dict(G.degree()).values()) / n

# Средняя степень вершины по формуле
theoretical_average_degree = (n - 1) * p

# Вывод результатов
print(f"Средняя степень вершины в сгенерированном графе: {average_degree:.2f}")
print(f"Средняя степень вершины по формуле: {theoretical_average_degree:.2f}")
