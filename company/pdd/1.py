"""
种地搜索
"""
n = 2
farm = [[0] * n for _ in range(n)]
crops = 6  # 6 种庄稼

ans = 0


def dfs(i, j, cnt):  # 种地数量?
    global ans
    if cnt == n * n:
        ans += 1
        return

    # 向右，向下 两个方向播种
    for c in range(1, crops + 1):
        if i > 0 and farm[i - 1][j] == c:  # 上面种 c, j=0 在这里一并处理了
            continue
        if j > 0 and farm[i][j - 1] == c:  # 左边种 c
            continue

        farm[i][j] = c  # 这个位置 种 c 作物
        # 指定二维情况下 dfs 搜索方向
        # i,j 移动会尝试不同的 c，最终达到 cnt 数量
        if j == n - 1:  # 列到头，去往下一行
            dfs(i + 1, 0, cnt + 1)
        else:  # 按列搜
            dfs(i, j + 1, cnt + 1)
        # 回溯
        farm[i][j] = 0

    return cnt


dfs(0, 0, 0)
print(ans)
