"""
https://leetcode-cn.com/problems/partition-equal-subset-sum/
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        转成 01 背包问题，是否存在一种组合，使得子集和 = sum(nums) / 2
        """
        total_s = sum(nums)
        if total_s % 2 != 0:  # 总和不是偶数 肯定不行
            return False

        n = len(nums)
        target_s = total_s // 2
        # 转化为 01 背包，选择每个商品是否采用
        # dp[i][j]: 前i个物品，背包容量 j 时存在一种方法恰好能将背包装满; 必须要让状态从 0 转移过来
        dp = [[False] * (target_s + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True  # 物品数 i，目标指令 0，满足

        for i in range(1, n + 1):  # 使用 n 个物品
            for j in range(1, target_s + 1):  # 总和
                if j - nums[i - 1] < 0:  # 物品 i 不能装
                    dp[i][j] = dp[i - 1][j]
                else:  # 不装 or 装，只要有个 True 即可
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            if dp[i][-1]:  # 前 i 个已经能达到目的，直接返回 True
                return True  # 利用 dp 数组，通过路径回溯 可找到要选的商品

        return False

    # 组合数思想，超出时间限制
    def canPartition_old(self, nums: List[int]) -> bool:
        """
        给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
        组合数思想，判断每个位置的值，是否使用
        """
        total_s = sum(nums)
        n = len(nums)

        def dfs(i, cur_s):  # 当前遍历到的位置 i，当前 sum
            x = 2 * cur_s
            if x == total_s:
                return True
            elif x > total_s:  # 超过 不满足
                return False
            if i == n:  # 遍历结束 也未满足
                return False

            # 使用 num[i] 或 不用; or 存在1个 True 即范围 True
            return dfs(i + 1, cur_s + nums[i]) or dfs(i + 1, cur_s)

        return dfs(0, 0)


s = Solution()
# nums = [1, 5, 11, 5]
nums = [1, 2, 3, 5]
# nums = [100] * 100 + [99, 97]
print(s.canPartition(nums))
print(s.canPartition_old(nums))  # [Previous line repeated 993 more times] maximum recursion depth exceeded in comparison
