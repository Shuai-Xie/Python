"""
DIJKSTRA(graph G, start vertex s,destination vertex d):
// all nodes initially unexplored

使用小顶堆结构，O(log(n)) 查询最小元素
let H = min heap data structure, initialized with 0 and s [here 0 indicates the distance from start vertex]
while H is non-empty:
    remove the first node and cost of H, call it U and cost
    if U is not explored
        mark U as explored
    if U is d:
        return cost // total cost from start to destination vertex
    for each edge(U, V): c=cost of edge(u,V) // for V in graph[U]
        if V unexplored:
            next=cost+c
            add next,V to H (at the end)
"""
import heapq  # 使 list 元素保持 min heap 结构


def dijkstra_A2B(graph, start, end):
    heap = [(0, start)]  # cost, node; 默认 heapq 字典序; 小顶堆
    S = set()  # 已找到最短路径的顶点集合

    while heap:
        cost, u = heapq.heappop(heap)  # 按照估计路径长度 作为 key 进行小顶堆排序
        if u in S:
            continue
        S.add(u)  # 加入集合，并对 经过 u 的邻接点的路径 进行松弛
        if u == end:
            return cost

        for v, w in graph[u]:
            if v not in S:  # 加入 heap，即进行 松弛
                heapq.heappush(heap, (cost + w, v))

    return -1


def dijkstra_A2all(graph, start):
    heap = [(0, start)]  # cost, node; 默认 heapq 字典序; 小顶堆
    dist = {}

    # 整个过程 S 不断地在扩充半径，每次引入刚刚进入圈内的点 u；然后以 u 松弛到 V-S 顶点的距离
    while heap:
        cost, u = heapq.heappop(heap)  # 按照估计路径长度 作为 key 进行小顶堆排序
        if u in dist:
            continue
        dist[u] = cost  # 保存找到的最短距离
        for v, w in graph[u]:
            if v not in dist:  # 加入 heap，即进行 松弛
                heapq.heappush(heap, (cost + w, v))
    return dist


G = {
    's1': [['s2', 30], ['s3', 15]],
    's2': [['s1', 5]],
    's3': [['s2', 10]]
}

print(dijkstra_A2B(G, 's1', 's2'))
print(dijkstra_A2all(G, 's1'))

G = {
    'A': [['B', 2], ['C', 5]],
    'B': [['A', 2], ['D', 3], ['E', 1]],
    'C': [['A', 5], ['F', 3]],
    'D': [['B', 3]],
    'E': [['B', 1], ['F', 3]],
    'F': [['C', 3], ['E', 3]]
}

print(dijkstra_A2B(G, 'A', 'D'))
print(dijkstra_A2all(G, 'A'))
