"""
输入
6
A B C D E E
A E D C B B

输出
0.33 Yes

最长公共，不要求连续, 暗含 可包含 多段公共序列?
s1,s2 长度相等
"""

N = int(input())
s1 = input().split()
s2 = input().split()

s1 = [''] + s1
s2 = [''] + s2

F = [[0] * (N + 1) for _ in range(N + 1)]

# F[i][j]:
# s1 到 i，s2 到 j 时，两条基因相似度
for i in range(1, N + 1):
    for j in range(1, N + 1):
        # 不一定来自上一状态，而是 之前所有匹配状态的 最大值 73%
        base = 0
        for k in range(i):
            for m in range(j):  # 要包括 F[1][1] 这样的场景
                base = max(base, F[k][m])
        F[i][j] = base + 1 if s1[i] == s2[j] else base  # 18%
        print(base, f'F[{i}][{j}]', F[i][j])

if N > 0:
    sim = F[N][N] / N
    if sim > 0.5:
        print('%.2f No' % sim)
    else:
        print('%.2f Yes' % sim)
