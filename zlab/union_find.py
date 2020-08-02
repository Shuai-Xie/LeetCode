from typing import List


class Solution:
    def union(self, i0, j0, i1, j1):
        root0 = self.find(i0, j0)
        root1 = self.find(i1, j1)
        self.parent[root1[0]][root1[1]] = root0

    def find(self, i, j):
        if self.parent[i][j] != (i, j):
            root = self.find(*self.parent[i][j])
            self.parent[i][j] = root
        return self.parent[i][j]

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) <= 0:
            return 0
        h, w = len(grid), len(grid[0])
        self.parent = [[(i, j) for j in range(w)] for i in range(h)]
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        for i in range(h):
            for j in range(w):
                if grid[i][j] != '1':
                    continue
                for d in range(4):
                    ti, tj = i + dx[d], j + dy[d]
                    if not (0 <= ti and ti < h and 0 <= tj and tj < w):
                        continue
                    if not grid[ti][tj] == '1':
                        continue
                    self.union(i, j, ti, tj)
        cnt = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1' and self.parent[i][j] == (i, j):
                    cnt += 1
        return cnt
