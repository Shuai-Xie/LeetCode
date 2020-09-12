from typing import List


class Solution:
    def cnt_01(self, s):
        cnt = {'0': 0, '1': 0}
        for c in s:
            cnt[c] += 1
        return cnt

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        每个 0/1 只能用1次，二维的01背包，问最多可拼成的 str 个数
        :param strs: 字符串数组，代表每个物品
        :param m: 0 个数
        :param n: 1 个数
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 行 0 个数，列 1 个数
        for s in strs:
            cnt = self.cnt_01(s)
            # dp 填表过程
            for i in range(m, cnt['0'] - 1, -1):
                for j in range(n, cnt['1'] - 1, -1):
                    dp[i][j] = max(
                        dp[i][j],  # 不装 s
                        dp[i - cnt['0']][j - cnt['1']] + 1  # 装 s
                    )
        return dp[-1][-1]


s = Solution()
strs = ["10", "0001", "111001", "1", "0"]
print(s.findMaxForm(strs, 5, 3))
strs = ["10", "0", "1"]
print(s.findMaxForm(strs, 1, 1))
