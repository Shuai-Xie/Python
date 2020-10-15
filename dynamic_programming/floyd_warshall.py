"""
https://wiki.jikexueyuan.com/project/easy-learn-algorithm/floyd.html
"""


def floyd_warshall(edges, V):
    # dp: 顶点对 (i,j) 间距离
    dp = [[float('inf')] * V for _ in range(V)]
    for i in range(V):
        dp[i][i] = 0

    # 根据 edges 初始化
    for u, v, w in edges:
        dp[u][v] = w

    # 选择引入中间节点 k，更新 i..j 距离
    for k in range(V):
        # 内层循环，组成任意顶点对
        # 并且更新完引入 0,...k-1 顶点的最优情况
        # dp[i][k] 暗含 i,k 两个顶点，中间已经过 0,...k-1 最优解
        # dp[k][j] 暗含 k,j 两个顶点，中间已经过 0,...k-1 最优解
        # 只要理解，这里的 k 其实也是 1..V 中某个顶点，并且 k-1 时刻最优距离已知
        for i in range(V):
            for j in range(V):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    print(dp)


V = 4

edges = [
    (0, 1, 2),
    (0, 2, 6),
    (0, 3, 4),
    (1, 2, 3),
    (2, 0, 7),
    (2, 3, 1),
    (3, 0, 5),
    (3, 2, 12)
]

floyd_warshall(edges, V)
