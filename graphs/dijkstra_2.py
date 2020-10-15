def find_u_with_minD(dist, S):
    # 从 dist 中找到估计距离最小的 u，并且 u 尚未在 S 中
    min_v = -1
    min_d = float('inf')
    for v, d in dist.items():
        if v not in S and d < min_d:
            min_d = d
            min_v = v
    return min_v


# 每次从 dist 找到离源点最近的一个顶点，并且此顶点没有加入 S
# 然后以该顶点为中心进行扩展，对能经过此顶点的路径进行放缩
# 最终得到源点到其余所有点的最短路径
def dijkstra(graph, start):
    """
    更新过程
        {'s1': 0, 's2': inf, 's3': inf}
        {'s1': 0, 's2': 30, 's3': 15}
        {'s1': 0, 's2': 25, 's3': 15}
    """
    V = len(graph)  # 节点个数
    S = set()
    dist = {v: float('inf') for v in G}  # 初始化节点距离
    dist[start] = 0  # 保存 start 到相应顶点的最小距离

    for i in range(V - 1):  # V-1 次，因为每次循环都会引入一个最近的点
        u = find_u_with_minD(dist, S)  # 每次都引入估计最近的点; 贪心
        S.add(u)
        for v, w in graph[u]:
            if v not in S and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    print(dist)


def dijkstra_minD(graph, start, end):
    V = len(graph)  # 节点个数
    S = set()
    dist = {v: float('inf') for v in G}  # 初始化节点距离
    dist[start] = 0  # 保存 start 到相应顶点的最小距离
    # dist 存储 最短路径的估计值; 每次选择最近顶点后，估计值 -> 确定值

    for i in range(V - 1):  # V-1 次，因为每次循环都会引入一个最近的点
        u = find_u_with_minD(dist, S)  # 每次都引入估计最近的点
        if u == end:
            return dist[u]
        S.add(u)
        for v, w in graph[u]:
            if v not in S and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist[end]


G = {
    's1': [['s2', 30], ['s3', 15]],
    's2': [['s1', 5]],
    's3': [['s2', 10]]
}

dijkstra(G, 's1')
print(dijkstra_minD(G, 's1', 's2'))
