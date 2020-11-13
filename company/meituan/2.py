"""

"""

# n: 参加总人数
# x: 指定晋级人数
# 求出实际晋级人数
n, x = list(map(int, input().split()))
scores = list(map(int, input().split()))


def wins(scores, n, x):
    # scores 为输入的 n 个得分
    scores = sorted(scores, reverse=True)  # 高到底
    # if n < x:
    #     x = n  # 确保不会超出

    # 第 x 人得分
    target = scores[x - 1]

    # if target > 0:  # 全部晋级
    #     return x

    cnt = 0
    for i in range(x):
        if scores[i] >= target and scores[i] > 0:
            cnt += 1

    # 可能存在第 x 人之后 还有相等的得分 可以晋级的?
    for i in range(x, n):
        if scores[i] == target and scores[i] > 0:
            cnt += 1
        else:
            break

    return cnt


print(wins(scores, n, x))
