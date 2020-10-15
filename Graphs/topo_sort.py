"""
Kahn's Algorithm is used to find Topological ordering of Directed Acyclic Graph using BFS
使用 bfs 的 topoSort
- bfs 层序遍历的特色，使得 toposort 结果，更具备易读性
- dfs 会以子树的形式遍历，单个子树完，再遍历另一个，层次先后并不明显

indegree 应用；每次遍历到一个节点，indegree-=1，边遍历边判断加入的节点
"""


def topoSort_bfs(l):
    indegree = [0] * len(l)
    queue = []
    topo = []
    cnt = 0

    # 入度
    for key, values in l.items():
        for i in values:
            indegree[i] += 1

    # 入度为 0 节点，可作为起始遍历节点
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        vertex = queue.pop(0)
        cnt += 1
        topo.append(vertex)
        for x in l[vertex]:
            indegree[x] -= 1
            if indegree[x] == 0:  # 邻接点的前驱任务都已完成时
                queue.append(x)

    if cnt != len(l):
        print("Cycle exists")
    else:
        print(topo)


def topoSort_dfs(l):
    indegree = [0] * len(l)
    stack = []
    topo = []
    cnt = 0

    # 入度
    for key, values in l.items():
        for i in values:
            indegree[i] += 1

    # 入度为 0 节点，可作为起始遍历节点
    for i in range(len(indegree)):
        if indegree[i] == 0:
            stack.append(i)  # 栈顶

    while stack:
        vertex = stack.pop()  # 栈顶都是入度=0 的
        topo.append(vertex)
        cnt += 1
        for x in l[vertex]:  # 邻接点
            indegree[x] -= 1
            if indegree[x] == 0:  # 入度=0，可以入栈; 若不等0，下次从别的路径过来，也能遍历到
                stack.append(x)

    if cnt != len(l):  # 当前面的 indegree=0 存在不满足时，这里加入
        print("Cycle exists")
    else:
        print(topo)


# Adjacency List of Graph
# 邻接链表
l1 = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [4, 5],
    4: [],
    5: []
}
l = {
    0: [1, 2],
    1: [],
    2: [6],
    3: [4, 5],
    4: [6],
    5: [],
    6: []
}
topoSort_bfs(l)
topoSort_dfs(l)
