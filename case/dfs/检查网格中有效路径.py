from typing import List


class Solution:
    def hasValidPath_save(self, grid: List[List[int]]) -> bool:
        # 节省 visited 内存，直接用 grid

        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            # 边界，结束 dfs
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if i == m - 1 and j == n - 1:
                return True

            # 符合情况
            # grid 值 指定可以前进的方向
            # 还要判断 转移方向的格子是否 与当前格子 连通

            tmp = grid[i][j]  # 记录方向
            grid[i][j] = -1  # 这样下次就不会走到了

            if tmp == 1:
                res1, res2 = False, False
                # 边界判断 and 方向连通 and 没有走过
                if 0 <= j - 1 < n and grid[i][j - 1] in [1, 4, 6]:  # 左
                    res1 = dfs(i, j - 1)
                if 0 <= j + 1 < n and grid[i][j + 1] in [1, 3, 5]:  # 右
                    res2 = dfs(i, j + 1)
                return res1 or res2
            elif tmp == 2:
                res1, res2 = False, False
                if 0 <= i - 1 < m and grid[i - 1][j] in [2, 3, 4]:  # 上
                    res1 = dfs(i - 1, j)
                if 0 <= i + 1 < m and grid[i + 1][j] in [2, 5, 6]:  # 下
                    res2 = dfs(i + 1, j)
                return res1 or res2
            elif tmp == 3:
                res1, res2 = False, False
                if 0 <= j - 1 < n and grid[i][j - 1] in [1, 4, 6]:  # 左
                    res1 = dfs(i, j - 1)
                if 0 <= i + 1 < m and grid[i + 1][j] in [2, 5, 6]:  # 下
                    res2 = dfs(i + 1, j)
                return res1 or res2
            elif tmp == 4:
                res1, res2 = False, False
                if 0 <= j + 1 < n and grid[i][j + 1] in [1, 3, 5]:  # 右
                    res1 = dfs(i, j + 1)
                if 0 <= i + 1 < m and grid[i + 1][j] in [2, 5, 6]:  # 下
                    res2 = dfs(i + 1, j)
                return res1 or res2
            elif tmp == 5:
                res1, res2 = False, False
                if 0 <= j - 1 < n and grid[i][j - 1] in [1, 4, 6]:  # 左
                    res1 = dfs(i, j - 1)
                if 0 <= i - 1 < m and grid[i - 1][j] in [2, 3, 4]:  # 上
                    res2 = dfs(i - 1, j)
                return res1 or res2
            elif tmp == 6:
                res1, res2 = False, False
                if 0 <= j + 1 < n and grid[i][j + 1] in [1, 3, 5]:  # 右
                    res1 = dfs(i, j + 1)
                if 0 <= i - 1 < m and grid[i - 1][j] in [2, 3, 4]:  # 上
                    res2 = dfs(i - 1, j)
                return res1 or res2

        return dfs(0, 0)

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # 1 <= m, n <= 300

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j):
            # 边界，结束 dfs
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if i == m - 1 and j == n - 1:
                return True

            # 符合情况
            visited[i][j] = True
            # grid 值 指定可以前进的方向
            # 还要判断 转移方向的格子是否 与当前格子 连通
            if grid[i][j] == 1:
                res1, res2 = False, False
                # 边界判断 and 方向连通 and 没有走过
                if 0 <= j - 1 < n and grid[i][j - 1] in [1, 4, 6] and not visited[i][j - 1]:  # 左
                    res1 = dfs(i, j - 1)
                if 0 <= j + 1 < n and grid[i][j + 1] in [1, 3, 5] and not visited[i][j + 1]:  # 右
                    res2 = dfs(i, j + 1)
                return res1 or res2
            elif grid[i][j] == 2:
                res1, res2 = False, False
                if 0 <= i - 1 < m and grid[i - 1][j] in [2, 3, 4] and not visited[i - 1][j]:  # 上
                    res1 = dfs(i - 1, j)
                if 0 <= i + 1 < m and grid[i + 1][j] in [2, 5, 6] and not visited[i + 1][j]:  # 下
                    res2 = dfs(i + 1, j)
                return res1 or res2
            elif grid[i][j] == 3:
                res1, res2 = False, False
                if 0 <= j - 1 < n and grid[i][j - 1] in [1, 4, 6] and not visited[i][j - 1]:  # 左
                    res1 = dfs(i, j - 1)
                if 0 <= i + 1 < m and grid[i + 1][j] in [2, 5, 6] and not visited[i + 1][j]:  # 下
                    res2 = dfs(i + 1, j)
                return res1 or res2
            elif grid[i][j] == 4:
                res1, res2 = False, False
                if 0 <= j + 1 < n and grid[i][j + 1] in [1, 3, 5] and not visited[i][j + 1]:  # 右
                    res1 = dfs(i, j + 1)
                if 0 <= i + 1 < m and grid[i + 1][j] in [2, 5, 6] and not visited[i + 1][j]:  # 下
                    res2 = dfs(i + 1, j)
                return res1 or res2
            elif grid[i][j] == 5:
                res1, res2 = False, False
                if 0 <= j - 1 < n and grid[i][j - 1] in [1, 4, 6] and not visited[i][j - 1]:  # 左
                    res1 = dfs(i, j - 1)
                if 0 <= i - 1 < m and grid[i - 1][j] in [2, 3, 4] and not visited[i - 1][j]:  # 上
                    res2 = dfs(i - 1, j)
                return res1 or res2
            elif grid[i][j] == 6:
                res1, res2 = False, False
                if 0 <= j + 1 < n and grid[i][j + 1] in [1, 3, 5] and not visited[i][j + 1]:  # 右
                    res1 = dfs(i, j + 1)
                if 0 <= i - 1 < m and grid[i - 1][j] in [2, 3, 4] and not visited[i - 1][j]:  # 上
                    res2 = dfs(i - 1, j)
                return res1 or res2

        return dfs(0, 0)


# grid = [[2, 4, 3], [6, 5, 2]]  # True
# grid = [[1, 2, 1], [1, 2, 1]]  # False
grid = [[1, 1, 2]]  # False

s = Solution()
print(s.hasValidPath(grid))
print(s.hasValidPath_save(grid))
