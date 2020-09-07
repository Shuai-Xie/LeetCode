from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # 陆地 0 水域 1
        m, n = len(grid), len(grid[0])

        # 封闭岛屿，必须是内部的，即 0 不能在边界处
        # 陆地边缘上下左右所有相邻区域都是水域; 只要求边缘是水，内部有水不影响

        if m <= 2 or n <= 2:  # 所有元素都能挨着边界，0个
            return 0

        def dfs(i, j):
            # 探索到边界
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return False
            if grid[i][j] == 1:  # 探索到水域，此位置到头，true，水域在边界也无所谓
                return True

            # 虽然是陆地 但是位于边界处，也是 false
            # 这一步不必要，因为当陆地能走到边界时，下一步自然就能出边界，返回 False
            # if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            #     grid[i][j] = 1  # 把陆地走掉
            #     return False

            # 探索到陆地
            grid[i][j] = 1  # 将走过的地方 变成水坑，下次就不会走了

            # 遍历四方；不能直接放在 and 中，会打断 dfs 向不同方向遍历，将 grid[i][j] 置1的过程
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)

            if up and down and left and right:
                return True
            else:
                return False

        cnt = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0 and dfs(i, j):  # 将 dfs 过程想象为染色
                    cnt += 1
        return cnt


grid = [[1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]]
# grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
# grid = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
#         [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
#         [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
#         [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
#         [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
#         [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
#         [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
#         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
#         [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]
s = Solution()
print(s.closedIsland(grid))
