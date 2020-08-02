from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        h, w = len(grid), len(grid[0])
        visited = [[0] * w for _ in range(h)]

        def dfs(i, j):
            if 0 <= i < h and 0 <= j < w and grid[i][j] == '1' and not visited[i][j]:
                visited[i][j] = 1
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

        cnt = 0

        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1' and not visited[i][j]:
                    cnt += 1
                    dfs(i, j)

        return cnt
