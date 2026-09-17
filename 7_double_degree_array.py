with open("rosalind_double_degree_array.txt") as file:
    n, m = map(int, file.readline().split())
    edges = []
    for line in file:
        edges.append(list(map(int, line.split())))

# graph = {}
# for i in range(1, n + 1):
#     graph[i] = []
graph = {i: [] for i in range(1, n + 1)} # словарь с ключами-вершинами

edges.sort()
print(edges)

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
print(graph)

double_degrees = [] # список для суммы степеней соседей
for i in range(1, n + 1):
    neighbor_degree_sum = 0
    for j in graph[i]:
        neighbor_degree_sum += len(graph[j])
    double_degrees.append(neighbor_degree_sum)
print(*double_degrees)