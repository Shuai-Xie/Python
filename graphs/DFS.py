"""
pseudo-code

DFS(graph G, start vertex s):
// all nodes initially unexplored
mark s as explored
for every edge (s, v):
    if v unexplored:
        DFS(G, v)
"""


def dfs(graph, start):
    stack = [start]
    visited = {}  # 使用有序字典保存遍历顺序

    while stack:
        u = stack.pop()
        visited[u] = None
        for v in graph[u]:  # 邻接点
            if v not in visited:
                stack.append(v)

    print(list(visited.keys()))


G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}

dfs(G, 'A')
