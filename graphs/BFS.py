"""
BFS(graph G, start vertex s):
// all nodes initially unexplored
mark s as explored
let Q = queue data structure, initialized with s
while Q is non-empty:
    remove the first node of Q, call it v
    for each edge(v, w):  // for w in graph[v]
        if w unexplored:
            mark w as explored
            add w to Q (at the end)

"""


def bfs(graph, start):
    queue = [start]
    visited = {}
    while queue:
        u = queue.pop(0)
        visited[u] = None
        for v in graph[u]:
            if v not in visited:  # 使用 dict 能判断 v 是否已经添加到候选，即完全是 white 状态
                queue.append(v)
    print(list(visited.keys()))


G = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(G, 'A')
