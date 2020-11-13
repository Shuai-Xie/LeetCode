"""
https://leetcode-cn.com/problems/subarray-sum-equals-k/

找出所有和为 k 的连续子数组
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

前缀和
"""
from typing import List


class Solution:
    def subarraySum_bf(self, nums: List[int], k: int) -> int:
        """
        所有和为 k 的连续子数组;
            通过记录前缀和，方便计算任意 i,j 之间子数组的和
            数组的长度为 [1, 20,000]
        """
        n = len(nums)

        # 前缀和 数组
        presum = [0]  # 方便计算子段
        for i in range(n):
            presum.append(presum[-1] + nums[i])

        # 计算任意 i,j 之间连续子序列之和
        cnt = 0
        # 穷举所有子数组
        for i in range(1, n + 1):
            for j in range(i):
                if presum[i] - presum[j] == k:
                    cnt += 1

        return cnt

    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0

        # 前缀和 : 出现次数
        presum = {0: 1}  # 从 nums[0] 之前开始算起
        sum0i = 0  # 还没加 nums[0] 状态

        # 遍历 nums, O(n)
        for i in range(n):
            sum0i += nums[i]  # 当前前缀和
            sum0j = sum0i - k  # 应有的 之前前缀和

            # 表示遍历到 i 位置时，又新增的更长的 满足的连续子序列
            if sum0j in presum:
                cnt += presum[sum0j]

            # 更新 sum0i 数量
            presum[sum0i] = presum.get(sum0i, 0) + 1

        return cnt


s = Solution()
nums = [1, 1, 1]
k = 2
print(s.subarraySum(nums, k))
