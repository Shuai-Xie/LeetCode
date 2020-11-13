"""
每天最多 n 个，各有1个正整数重量
已做好 m 个
买 最重 最轻 a,b; 保证 a/b 大小关系
剩余 n - m 在烤
"""


# 不保证 a/b 大小关系
# 1 ≤ n,m,a,b ≤ 1000 , m≤n , 蛋糕重量不会超过1000


def cake():
    vmax, vmin = max(arr), min(arr)
    tmax, tmin = max(a, b), min(a, b)

    # 已做出的蛋糕 不满足要求
    if vmax > tmax or vmin < tmin:
        return 'NO'

    # 仍在区间内
    remain = n - m

    if remain == 0:
        if vmax == tmax and vmin == tmin:  # 比如两个都相等
            return 'YES'
        else:
            return 'NO'
    elif remain == 1:
        if vmax == tmax or vmin == tmin:  # 只要有1个已经相等 即可
            return 'YES'
        else:
            return 'NO'
    else:  # 仍在区间内，并且还有两个能做
        return 'YES'


while True:
    n, m, a, b = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(cake())
