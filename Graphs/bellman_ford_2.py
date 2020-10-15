# G = {
#     's1': [['s2', 30], ['s3', 15]],
#     's2': [['s1', 5]],
#     's3': [['s2', 10]]
# }

G = {
    'S': [['A', 1], ['B', 2]],
    'A': [['B', 2]],
    'B': [['A', -2]]  # 可处理负权边; -2+2=0,没形成负权环
}


def bellman_ford(graph, start):
    # 1: initialize graph
    dist = {k: float('inf') for k in graph}
    dist[start] = 0

    edges = []
    for u, items in G.items():
        for v, w in items:
            edges.append((u, v, w))
    V = len(G)

    # 2: relax edges repeatedly
    # At each iteration i that the edges are scanned,
    # the algorithm finds all shortest paths of at most length i edges (and possibly some paths longer than i edges).
    # Since the longest possible path without a cycle can be V-1 edges,
    # the edges must be scanned V-1 times to ensure the shortest path has been found for all nodes.
    for i in range(V - 1):  # 已确定1个节点 s，还剩 V-1
        # 每次迭代，能找到 最多由 i 条边组成的 最短路径
        # 考虑到最长路径可以是 V-1 条边，所以迭代 V-1 次; 因为事先不知道图结构，所以执行 V-1
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # 3: check for negative-weight cycles
    # A final scan of all the edges is performed and
    # if any distance is updated, 如果更新，说明发现使用 V 条边的最短路径
    # then a path of length V edges has been found which can only occur if at least one negative cycle exists in the graph.
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Negative cycle found. Solution not possible.")
            return

    print(dist)


bellman_ford(G, 'S')
