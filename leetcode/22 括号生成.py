"""
数字 n 代表生成括号的对数，请你设计一个函数，
用于能够生成所有可能的并且 有效的 括号组合。

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        ans = ''

        # 有约束的全排列问题
        def dfs(i=0, s1=0, s2=0):  # 左右括号使用个数
            nonlocal ans
            if i == n * 2:  # 到末尾了
                res.append(ans)

            if s1 < n:
                ans += '('
                s1 += 1
                dfs(i + 1, s1, s2)
                ans = ans[:-1]
                s1 -= 1

            if s2 < n and s1 > s2:  # ')' 不能单独出现
                ans += ')'
                s2 += 1
                dfs(i + 1, s1, s2)
                ans = ans[:-1]
                s2 -= 1

        dfs()
        return res


s = Solution()
print(s.generateParenthesis(3))
