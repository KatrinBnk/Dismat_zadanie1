import numpy as np

# Возведение матрицы в степень.
def raise_matrix_to_power(matrix, power):
    return np.linalg.matrix_power(matrix, power)

# Расчёт расстояний и количества путей заданной длины между вершинами.
def calculate_paths_and_distance(adjacency_matrix, start_vertex, end_vertex, path_length):
    # ПОМЕТКА. Для поиска кратчайшего пути матрицу возводим в степень 1, то есть не изменяем
    # Возводим матрицу смежности в степень, соответствующую длине пути
    matrix_power = raise_matrix_to_power(adjacency_matrix, path_length)

    # Получаем количество путей заданной длины между начальной и конечной вершинами
    num_paths = matrix_power[start_vertex, end_vertex]

    # Ищем кратчайший путь
    for i in range(1, len(adjacency_matrix)):
        if raise_matrix_to_power(adjacency_matrix, i)[start_vertex, end_vertex] > 0:
            shortest_path_length = i
            break
    else:
        shortest_path_length = float('inf')  # Если путь не найден

    return shortest_path_length, num_paths

# Ввод матрицы пользователем через консоль
def input_adjacency_matrix():
    num_vertices = int(input("Введите количество вершин графа: "))
    print("Введите матрицу смежности (каждую строку вводите отдельно, разделяя числа пробелами):")
    matrix = [list(map(int, input().split())) for _ in range(num_vertices)]

    return np.array(matrix)

# Вычисление количества ребер введенной матрицы
def calculate_edges(matrix):
    return np.sum(matrix) // 2

def user_input_vertices(prompt):
    start_vertex, end_vertex = map(int, input(prompt).split())
    return (start_vertex, end_vertex)


adjacency_matrix = input_adjacency_matrix()

num_edges = calculate_edges(adjacency_matrix)

# Получаем вершины от пользователя для расчета кратчайшего пути
start_vertex, end_vertex = user_input_vertices("Введите две вершины для определения кратчайшего расстояния(ввод через пробел): ")
shortest_path_length, _ = calculate_paths_and_distance(adjacency_matrix, start_vertex-1, end_vertex-1, 1)
print(f"Кратчайший путь между вершинами ({start_vertex}, {end_vertex}): {shortest_path_length}")

# Получаем другие две вершины от пользователя для расчета путей заданной длины
start_vertex_path, end_vertex_path = user_input_vertices("Введите две вершины для расчета путей определенной длины(ввод через пробел): ")
path_length = num_edges - len(adjacency_matrix) + 3
_, num_paths_specific_length = calculate_paths_and_distance(adjacency_matrix, start_vertex_path-1, end_vertex_path-1, path_length)
print(f"Количество путей длиной {path_length} между вершинами ({start_vertex_path}, {end_vertex_path}): {num_paths_specific_length}")