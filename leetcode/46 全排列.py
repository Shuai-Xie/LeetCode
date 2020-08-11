"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
"""
from typing import List




class Solution:
    # dfs 回溯: 回到之前状态的意思
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []
        used = [False] * n

        def dfs(depth):
            if depth == len(nums):  # 已经到最后一层
                res.append(path[:])  # copy path 对象
                return
            # n 数字顺序，恰好为字典序
            for i in range(n):
                # 用 used 保存每个 i 使用状态，不必每次到 path 中去查找
                if used[i]:  # 如果使用了
                    continue
                # 如果 i 还没用
                path.append(nums[i])
                used[i] = True
                # 寻找下一个元素
                dfs(depth + 1)
                # 回溯，重置状态
                path.pop()  # 移除最后1个
                used[i] = False

        dfs(0)
        return res


s = Solution()
a = s.permute([1, 2, 5, 5])
print(len(a))
print(a)
