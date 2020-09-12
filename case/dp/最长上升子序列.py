from typing import List


class Solution:

    def get_one_LIS(self, dp):
        """
        获得任意一个 LIS
            dp[i] 其实记录了 每个元素 在 LIS 序列中的位置，可以按照值的大小反向找回去
        """
        n = len(dp)
        cur_len = max(dp)
        ans = []

        for i in range(n - 1, -1, -1):  # 倒着索引
            if dp[i] == cur_len:
                ans.append(nums[i])
                cur_len -= 1
                if cur_len == 0:
                    break
        return ans[::-1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        最长上升子序列, 不要求连续
            dp[i]: 以 nums[i] 结尾的 LIS 长度
                   注意：指的是 nums[i] 作为最大元素的情况，因为 状态转移
        状态转移:
         0<=j < i
            dp[i] = max(d[j]) +1, 如果 nums[j] < nums[i] 严格上升
        """
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n  # 初始化，n=1 的情况刚好包含在内

        for i in range(1, n):
            for j in range(i):  # i 之前的某个字符
                if nums[i] > nums[j]:  # 更新情况
                    dp[i] = max(dp[i], dp[j] + 1)  # j 位置最长 +1

        print(self.get_one_LIS(dp))

        return max(dp)


s = Solution()
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
print(s.lengthOfLIS(nums))
