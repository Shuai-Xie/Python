"""
MST Minimum Spanning Tree
贪心思想
    Kruskal: 寻找连接 森林中 两棵子树的 权值最小的边; 子树的代表 节点
    Prim: 寻找子树 A 连接外部顶点中 权值最小的边
"""

# P363
# 无向图的最小生成树
num_v = 9
edges = [
    # node1, node2, cost
    ['a', 'b', 4],
    ['a', 'h', 8],
    ['b', 'c', 8],
    ['b', 'h', 11],
    ['c', 'd', 7],
    ['c', 'f', 4],
    ['c', 'i', 2],
    ['d', 'e', 9],
    ['d', 'f', 14],
    ['e', 'f', 10],
    ['f', 'g', 2],
    ['g', 'h', 1],
    ['g', 'i', 6],
    ['h', 'i', 7],
]

edges = sorted(edges, key=lambda t: t[-1])  # 按 cost 排序
parent = list(range(num_v))  # tricks: 使用 parent 数组表示节点 是否属于同一个连通分量(子树)


def char2idx(c):  # 字母映射到下标
    return ord(c) - ord('a')


def find_parent(idx):  # 节点编号
    if idx == parent[idx]:  # 当前节点即为代表节点
        return idx
    return find_parent(parent[idx])  # 向上寻找代表节点


def Kruskal():
    mst_cost = 0
    mst = []
    cnt = 0

    # 每次都选择一条最短的边 连接两个子树，形成新的树
    for e in edges:  # cost 排过序的
        a, b, cost = e
        pa = find_parent(char2idx(a))
        pb = find_parent(char2idx(b))

        if pa != pb:
            mst_cost += cost
            mst.append(e)
            parent[pa] = pb  # 将 a 树作为 b 树的子树
            cnt += 1
            if cnt == num_v - 1:  # 树: 顶点数 = 边数 + 1
                break

    print(mst_cost)
    print(sorted(mst))


Kruskal()
