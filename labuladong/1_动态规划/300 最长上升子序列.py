"""
https://leetcode-cn.com/problems/longest-increasing-subsequence/
给定一个无序的整数数组，找到其中最长上升子序列的长度。 没有要求连续

可以看到
    要求子数组连续的问题，如最长连续上升子序列，最大连续子序和，都是 O(n)
    非连续的问题，lengthOfLIS 是 O(n^2)
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 最长上升子序列
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n  # 初始化最长，单个元素为一个子数组
        for i in range(1, n):
            for j in range(i):  # 当前位置之前的元素
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 在 j 基础上 + 当前元素 i

        return max(dp)

    def lengthOfContinueLIS(self, nums: List[int]) -> int:
        # 最长连续上升子序列
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n  # 初始化最长，单个元素为一个子数组
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)


s = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(s.lengthOfLIS(nums))
print(s.lengthOfContinueLIS(nums))
