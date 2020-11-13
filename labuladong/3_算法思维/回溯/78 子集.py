"""
https://leetcode-cn.com/problems/subsets/
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集)
解集不能包含重复的子集

子集数量 = 2^n 个
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        不重复元素的子集，就是在判断不同长度的 组合数
        组合数规则：
            递归模拟 组合数抽样过程 位置 i 元素选还是不选
            就已经涵盖了所有长度的组合
        """
        ans = []
        path = []

        n = len(nums)

        def dfs(i):  # 当前遍历到的位置
            if path not in ans:  # 通过 O(n) 查找去重
                ans.append(path[:])
            if i == n:  # 添加 path 后还可继续遍历其他长度，递归出口为遍历完到数组末尾
                return
            # 使用当前元素
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
            # 不用当前元素
            dfs(i + 1)

        dfs(0)
        return ans

    def subsets_old(self, nums: List[int]) -> List[List[int]]:
        ans = []

        n = len(nums)
        used = [False] * n

        path = []

        # 全排列的方式，复杂度太高，会超时
        def dfs(d):
            nonlocal path
            b = sorted(path)  # 这里切勿用 path 接收，会影响之后的 path.pop() 得到错误的结果
            if b not in ans:
                ans.append(b)

            if d == n:  # 结束递归
                return

            for i in range(n):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(d + 1)
                path.pop()
                used[i] = False

        dfs(0)  # 只 dfs 一次即可; 因为 path 搜索过程中 长度就在逐步增加了

        return ans


s = Solution()
nums = [1, 2, 3]
sub = s.subsets(nums)
print(sub)
sub = s.subsets_old(nums)
print(sub)
