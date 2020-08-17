"""
输入
6
A B C D E E
A E D C B B

输出
0.33 Yes

最长公共，不要求连续, 暗含 可包含 多段公共序列?
s1,s2 长度相等

字符串的子序列：
原字符串在 不改变字符的相对顺序的情况下 删除某些字符（也可以不删除任何字符）后组成的新字符串; 已暗含 可以不连续
如 "ace" 是 "abcde" 的子序列
"""

# N = int(input())
# s1 = input()
# s2 = input()
s1 = 'ABCDEE'
s2 = 'ABEDCDBB'
s1 = '#' + s1
s2 = '#' + s2
m, n = len(s1), len(s2)


# longestCommonSubsequence, 2D DP
def LCS():  # 要求连续
    f = [[0] * n for _ in range(m)]
    # f[i][j]: s1 长度 i, s2 长度 j 的公共长度
    for i in range(1, m):
        for j in range(1, n):
            # 只描述某个状态的解决方案，认为子问题会计算得到正确的解
            if s1[i] == s2[j]:
                f[i][j] = f[i - 1][j - 1] + 1
            else:
                f[i][j] = max(f[i][j - 1], f[i - 1][j])
    return f[-1][-1]


# 暴力法 O(n^3), i, j 截取，向前索引


def LCS_continue():  # 最长公共子串, 要求公共子序列连续
    f = [[0] * n for _ in range(n)]
    # f[i][j]: 以 s1[i],s2[j] 为末尾 char 的子序列，就包括了所有组合
    # 终止符是否出现
    s1_end, s2_end = [False] * m, [False] * n
    max_val = 0
    max_pos = []
    for i in range(1, m):
        for j in range(1, n):
            if s1[i] == s2[j]:
                f[i][j] = f[i - 1][j - 1] + 1
                if f[i][j] > max_val:
                    max_val = f[i][j]
                    max_pos = [(i, j)]  # update
                    s1_end, s2_end = [False] * m, [False] * n
                    s1_end[i], s2_end[j] = True, True
                elif f[i][j] == max_val:
                    # 去重，任一终止符位置 相同，必然 substr 相同
                    # 要求 两个终止符 都未出现
                    if not s1_end[i] and not s2_end[j]:
                        max_pos.append((i, j))  # add
                        s1_end[i], s2_end[j] = True, True

    print(max_val)
    print(max_pos)
    res = []
    for p1, p2 in max_pos:
        res.append(s1[p1 - max_val + 1:p1 + 1])
    print(res)


def merge_two_list(l1, l2):
    # 去重合并2个list
    li = l1 + l2
    if len(l1) > 0:
        li.sort()
        res = [li[0]]
        for i in range(1, len(li)):
            if li[i] == li[i - 1]:
                continue
            res.append(li[i])
        return res
    return []


def LCS_res():
    f = [[0] * n for _ in range(m)]
    res = [[[] for _ in range(n)] for _ in range(m)]

    # F[i][j]:
    # s1 到 i，s2 到 j 时，两条基因相似的 chars
    for i in range(1, m):
        for j in range(1, n):
            # 不一定来自上一状态，而是 之前所有匹配状态的 最大值 73%
            if s1[i] == s2[j]:
                f[i][j] = f[i - 1][j - 1] + 1
                if res[i - 1][j - 1]:
                    res[i][j] += [s + s1[i] for s in res[i - 1][j - 1]]  # 保存所有可行解
                else:
                    res[i][j].append(s1[i])  # 为空另外处理
            else:
                if f[i][j - 1] > f[i - 1][j]:
                    f[i][j] = f[i][j - 1]
                    res[i][j] = res[i][j - 1]
                elif f[i][j - 1] < f[i - 1][j]:
                    f[i][j] = f[i - 1][j]
                    res[i][j] = res[i - 1][j]
                else:  # 两个相等, 虽然相等 但是组成元素可能不同
                    f[i][j] = f[i - 1][j]
                    # res[i][j] = list(set(res[i - 1][j]) | set(res[i][j - 1]))
                    res[i][j] = merge_two_list(res[i - 1][j], res[i][j - 1])

    print(f[-1][-1])
    print(res[-1][-1])


def LCS_space():
    dp = [0] * n  # 空间压缩
    for i in range(m):
        tmp = 0
        for j in range(1, n):
            if s1[i] == s2[j]:
                dp_j = tmp + 1
            else:  # dp[j] 对应上一轮 d[i-1][j], 而 d[j-1] 对应 d[i][j-1]
                dp_j = max(dp[j], dp[j - 1])  # dp[i][j]
            tmp = dp[j]
            dp[j] = dp_j
    return dp[-1]


if __name__ == '__main__':
    print('LCS_continue')
    LCS_continue()
    print()
    print('LCS_res')
    LCS_res()
