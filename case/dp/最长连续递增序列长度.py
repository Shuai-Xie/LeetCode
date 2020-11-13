"""
https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/
"""
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = max(dp[i], dp[i - 1] + 1)  # 在 i-1 长度基础上 +1

        return max(dp)


s = Solution()
# nums = [1, 3, 5, 4, 7]
nums = [2, 2, 2, 2, 2]
print(s.findLengthOfLCIS(nums))
