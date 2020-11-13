"""
https://leetcode-cn.com/problems/longest-common-subsequence/

给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j]: text1[:i] 和 text2[:j] 公共子序列长度
        l1, l2 = len(text1), len(text2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:  # 若相等
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  # 不相等情况，对于之前状态的选择，传递过程
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


s = Solution()
# text1 = "abcde"
# text2 = "ace"
text1 = "abc"
text2 = "def"
print(s.longestCommonSubsequence(text1, text2))
