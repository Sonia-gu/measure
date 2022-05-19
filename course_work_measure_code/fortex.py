#функция поска в глубину в графе
def dfs(adjacency, vertex, visited = None, path = None): 
    if visited is None:
        visited = set()
    if path is None:
        path = []     
    visited.add(vertex)
    path.append(vertex)
    if vertex in adjacency:
        for neighbor in adjacency[vertex]:
            if neighbor not in visited:
                dfs(adjacency, neighbor, visited, path)
    return path

#функция поска циклов в графе
def cicle_search(graph, v):
    cicle = dict()
    visited=set()
    for vi in v:
        if vi in visited: continue
        else: 
            cicle[vi] = dfs(graph, vi)
            for vj in cicle[vi]: visited.add(vj)
    return [c for c in cicle.values()]

# преобразование Т
def T(x):
    return (2*x + 3)%7

#заданная на X функция
def f(x):
    return x**2
#задание графа преобразования
X = np.array([0, 1, 2, 3, 4, 5, 6])
graph = dict()
for x in X:
    graph[x] = [T(x)]
#поиск циклов
cicles = cicle_search(graph, X)
print(cicles)
#[[0, 3, 2], [1, 5, 6], [4]]

#построение изображения
fig = plt.figure(figsize=(6, 6))
# свой цвет для каждого цикла
cicle_colors = ['b', 'royalblue', 'darkblue'] 
# момент до которого вычисляем 
N = 30 
#T^0(X), f(X)
Tn_X = X.copy() 
fTn = f(Tn_X)
for n in range(1, N):
    #T^n(X), \sum_{i=1}^{n-1}f(T^i X)
    Tn_X = T(Tn_X)
    fTn+=f(Tn_X) 
    # n-e эргодическое среднее
    Anf = fTn/n
    for i, c in enumerate(cicles):
        plt.scatter(c, Anf[c], color = cicle_colors[i])

# просто среднее значение f на цикле
for i, c in enumerate(cicles):
    av = [sum(f(np.array(c)))/len(c) for k in range(len(c))]
    plt.plot(c, av, marker = 's', linestyle = '--', color = cicle_colors[i])

plt.grid()
plt.savefig('example1.png')