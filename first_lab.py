import heapq

#Алгоритм для матрицы смежности
def dijkstra_matrix(graph, start):
    #число вершин в графе
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        # Извлекаем вершину с минимальным расстоянием
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        # Помечаем вершину как посещенную
        visited.add(current_vertex)

        for neighbor, weight in enumerate(graph[current_vertex]):
            # Если есть ребро между current_vertex и neighbor
            if weight > 0:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    #Добавляем соседнюю вершину с новым расстоянием
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances


#Алгоритм для списка смежностей
def dijkstra_adj_list(adj_list, start):
    distances = {vertex: float('inf') for vertex in adj_list}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        # Извлекаем вершину с минимальным расстоянием
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in adj_list[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Функция определяет тип графа и вызывает соответствующую функцию
def dijkstra(graph, start):
    #Проверка, что граф задан матрицей смежностей
    if isinstance(graph, list) and all(isinstance(row, list) for row in graph):
        return dijkstra_matrix(graph, start)
    #Проверка, что граф задан списком смежностей
    elif isinstance(graph, dict):
        return dijkstra_adj_list(graph, start)
    else:
        raise ValueError(
            "Неизвестный формат графа. Ожидается матрица смежности (list of lists) или список смежности (dict)")


# Граф в виде матрицы смежности
graph_matrix = [
    [0, 10, 0, 5, 0],
    [10, 0, 1, 2, 0],
    [0, 1, 0, 0, 7],
    [5, 2, 0, 0, 3],
    [0, 0, 7, 3, 0]
]

# Граф в виде списка смежности
graph_adj_list = {
    0: [(1, 10), (3, 5)],
    1: [(0, 10), (2, 1), (3, 2)],
    2: [(1, 1), (4, 7)],
    3: [(0, 5), (1, 2), (4, 3)],
    4: [(2, 7), (3, 3)]
}

#Вывод кратчайших путей для матрицы смежности
start_vertex = 4
print(f"Кратчайшие расстояния от вершины {start_vertex} (матрица смежности):")
distances_matrix = dijkstra(graph_matrix, start_vertex)
for i, dist in enumerate(distances_matrix):
    print(f"До вершины {i}: {dist}")

#Вывод кратчайших путей для списка смежностей
print(f"\nКратчайшие расстояния от вершины {start_vertex} (список смежности):")
distances_adj = dijkstra(graph_adj_list, start_vertex)
for vertex, dist in distances_adj.items():
    print(f"До вершины {vertex}: {dist}")