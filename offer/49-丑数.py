"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
- 质因子只有 2,3,5，不要求全部存在
- 1 是丑数

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。所以第10个输出 12

丑数的递推性质：
丑数只包含因子 2, 3, 5，因此有 “丑数 = 某较小丑数 × 某因子” （例如：12 = 6 * 2）。
"""


class Solution:
    def nthUglyNumber_v1(self, n: int) -> int:
        nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

        i2, i3, i5 = 0, 0, 0  # 2,3,5 对应的下标
        for i in range(10, n):
            last = nums[-1]  # x_n

            # 先找到 所有 i2,i3,i5，再求；比较耗时
            while nums[i2] * 2 <= last:  # 直到 *2 能 > last
                i2 += 1
            while nums[i3] * 3 <= last:
                i3 += 1
            while nums[i5] * 5 <= last:
                i5 += 1

            nums.append(min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5))

        return nums[n - 1]

    def nthUglyNumber(self, n: int) -> int:
        # 不用去把 i2,i3,i5 都找到
        dp = [1] * n
        i2, i3, i5 = 0, 0, 0  # 2,3,5 对应的下标
        for i in range(1, n):
            n2, n3, n5 = dp[i2] * 2, dp[i3] * 3, dp[i5] * 5
            dp[i] = min(n2, n3, n5)
            # 不+1 下个丑数一定不满足
            if dp[i] == n2:
                i2 += 1
            if dp[i] == n3:
                i3 += 1
            if dp[i] == n5:
                i5 += 1

        return dp[n - 1]


s = Solution()
for i in range(1, 20):
    print(s.nthUglyNumber(i))
