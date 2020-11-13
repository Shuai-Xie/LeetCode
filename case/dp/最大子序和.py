"""
https://leetcode-cn.com/problems/maximum-subarray/
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """ 最大连续子序列和问题
        dp[i]: 以 nums[i] 为结尾的 最大子序列和
            dp[i] = max(dp[i-1] + nums[i], dp[i-1])
            选择 nums[i] 是否要加入之前的子序
        """
        n = len(nums)
        if n == 0:
            return n

        dp = [0] * n
        dp[0] = nums[0]  # 要求子数组最少包含1个元素，所以如果首位为负数，不能通过不选返回0
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)


s = Solution()
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [1]
print(s.maxSubArray(nums))
