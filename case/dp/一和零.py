"""
https://leetcode-cn.com/problems/ones-and-zeroes/
m 个 0, n 个 1; 能拼成数组中 字符串的 最大数量
"""

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # strs 中的 s 同时消耗 0/1 两种商品; 0/1 背包; 选择 s 是否放入
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        def cnt01(s):
            cnt = {'0': 0, '1': 0}
            for c in s:
                cnt[c] += 1
            return cnt['0'], cnt['1']

        for s in strs:
            cnt0, cnt1 = cnt01(s)  # m,n
            for i in range(m, cnt0 - 1, -1):
                for j in range(n, cnt1 - 1, -1):  # 大到小更新，小的恰好是不包含当前 s 时，能得到的最优状态
                    dp[i][j] = max(dp[i][j], dp[i - cnt0][j - cnt1] + 1)

        return dp[-1][-1]


strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3

strs = ["10", "0", "1"]
m = 1
n = 1

s = Solution()
print(s.findMaxForm(strs, m, n))
