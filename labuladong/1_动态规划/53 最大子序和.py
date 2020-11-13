"""
https://leetcode-cn.com/problems/maximum-subarray/
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 连续的子数组
        n = len(nums)
        dp = nums[:]  # 初始状态，单个元素即一个子数组
        # dp[i] 以 i 结尾的最大子序和

        for i in range(1, n):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])

        return max(dp)


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(nums))
