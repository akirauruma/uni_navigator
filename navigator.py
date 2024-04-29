import matplotlib.pyplot as plt


# Функция для отображения графа с учетом пути
def plot_graph_with_path(graph, vertices, path):
    # Создание нового графического окна
    plt.figure()

    # Отрисовка вершин
    for vertex, coords in vertices.items():
        plt.scatter(coords[0], coords[1], color='blue')  # Отображаем вершину как точку с координатами из словаря

    # Отрисовка рёбер
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            # Получаем координаты начальной и конечной вершин для ребра
            start_coords = vertices[vertex]
            end_coords = vertices[neighbor]
            # Отрисовка ребра
            plt.plot([start_coords[0], end_coords[0]], [start_coords[1], end_coords[1]], color='black')

    # Добавление названий вершин
    for vertex, coords in vertices.items():
        plt.text(coords[0], coords[1], vertex, fontsize=12, ha='center', va='center')

    # Отрисовка пути
    if path:
        for i in range(len(path) - 1):
            start_coords = vertices[path[i]]
            end_coords = vertices[path[i + 1]]
            plt.plot([start_coords[0], end_coords[0]], [start_coords[1], end_coords[1]], color='red',
                     linestyle='dashed')

    # Настройка осей и отображение графа
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('University Map Graph')
    plt.grid(True)
    plt.show()

# Пример данных вершин и рёбер
vertices = {
    'path_1': (1197, -1247),
    'path_2': (1350, -924),
    'path_3': (1350, -675),
    'path_4': (1350, -525),
    'path_5': (1350, -166),
    '103':	(1337, -846),
    '104':	(1337, -782),
    '105':	(1337, -752),
    '106':	(1337, -708),
    '107':	(1337, -654),
    '108':	(1337, -613),
    '109':	(1337, -580),
    '110':	(1337, -550),
    '111':	(1337, -473),
    '112А':	(1337,	-422),
    '112Б':	(1337,	-368),
    '113А':	(1337,	-314),
    '114':	(1337, -218),
    '115':	(1337, -187),
    '127':	(1363,	-877),
    '126':	(1363,	-846),
    '125':	(1363,	-781),
    '124':	(1363,	-708),
    '123':	(1363,	-657),
    '122':	(1363,	-549),
    '121':	(1363,	-517),
    '120':	(1363,	-474),
    '119':	(1363,	-422),
    '118':	(1363,	-367),
    '117':	(1363,	-267)
}

edges = [
    ('path_1', 'path_2'),
    ('path_2', 'path_3'),
    ('path_3', 'path_4'),
    ('path_4', 'path_5'),
    ('path_5', '114'),
    ('path_5', '115')
]

# Пример пути
path = ['path_1', 'path_2', 'path_3', 'path_4', 'path_5', '114']

# Создание пустого графа
graph = {}

# Добавление вершин в граф
for vertex, coords in vertices.items():
    graph[vertex] = []

# Добавление рёбер в граф
for i in range(len(path) - 1):
    start = path[i]
    end = path[i + 1]
    graph[start].append(end)
    graph[end].append(start)  # Добавляем обратное ребро для неориентированного графа

# Вызов функции для отображения графа с учетом пути
plot_graph_with_path(graph, vertices, path)
