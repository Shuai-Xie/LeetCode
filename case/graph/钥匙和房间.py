"""
https://leetcode-cn.com/problems/keys-and-rooms/
判断能否 进入所有的房间
"""

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n

        # 开始只有 0 号房门
        def dfs(i):
            if visited[i]:
                return
            visited[i] = True
            for k in rooms[i]:
                dfs(k)

        dfs(0)
        return all(visited)


# rooms = [[1], [2], [3], []]
rooms = [[1, 3], [3, 0, 1], [2], [0]]
s = Solution()
print(s.canVisitAllRooms(rooms))
