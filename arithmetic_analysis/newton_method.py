"""
https://en.wikipedia.org/wiki/Newton%27s_method
关注 维基百科中 解的从两边向中间不断节点的更新过程

x_n+1 = x_n - f(x_n) / f'(x_n)
"""


# 原函数
def f(x):
    return (x ** 3) - (2 * x) - 2


# 一阶导数
def f1(x):
    return 3 * (x ** 2) - 2


def newton(f, f1, start_val):
    x = start_val
    while True:
        x1 = x - f(x) / f1(x)
        if abs(x - x1) < 1e-6:
            return x1
        x = x1  # 迭代更新 x1


if __name__ == "__main__":
    print(newton(f, f1, 3))  # 可先估计一个值，然后不断靠近
