from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m, n = len(land), len(land[0])  # 行，列

        def dfs(i, j):
            nonlocal cnt
            # 边界
            if i < 0 or i >= m:
                return
            if j < 0 or j >= n:
                return
            # 之前访问过的水域 or 陆地
            if land[i][j] == -1 or land[i][j] > 0:  # land[i][j] != 0
                return

            if land[i][j] == 0:  # 可访问
                cnt += 1
                land[i][j] = -1  # 染色
                # 垂直，水平，或 对角线, 8 邻域
                dfs(i - 1, j - 1)
                dfs(i - 1, j)
                dfs(i - 1, j + 1)
                dfs(i, j - 1)
                dfs(i, j + 1)
                dfs(i + 1, j - 1)
                dfs(i + 1, j)
                dfs(i + 1, j + 1)

        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:  # 未被访问
                    cnt = 0
                    dfs(i, j)
                    res.append(cnt)

        return sorted(res)


s = Solution()
land = [
    [0, 2, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1]
]
print(s.pondSizes(land))
