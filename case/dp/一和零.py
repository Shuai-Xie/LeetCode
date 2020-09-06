from typing import List


class Solution:
    def cnt_zero_ones(self, s):
        cnt = {'0': 0, '1': 0}
        for c in s:
            cnt[c] += 1
        return cnt

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 二维背包问题，每次选择1个s，要同时消耗 0/1 两种费用
        # dp[i][j]: i个0,j个1 能容纳的最多字符串数量; 再多的维度只要增加保存的状态即可
        # 有限01背包问题，每个 str 只能放一次
        # m,n 两个容量约束，2D 的01背包问题

        for s in strs:
            cnt = self.cnt_zero_ones(s)
            # 针对 s 判断 放还是不放
            for zeros in range(m, cnt['0'] - 1, -1):  # 0 数目从大到小
                for ones in range(n, cnt['1'] - 1, -1):  # 1 数目从大到小
                    dp[zeros][ones] = max(
                        dp[zeros][ones],  # 遇见 s 之前 此容量最佳状态
                        dp[zeros - cnt['0']][ones - cnt['1']] + 1,  # 选择装 s 后的 状态
                    )

        return dp[m][n]


s = Solution()
strs = ["10", "0001", "111001", "1", "0"]
print(s.findMaxForm(strs, 5, 3))
strs = ["10", "0", "1"]
print(s.findMaxForm(strs, 1, 1))
