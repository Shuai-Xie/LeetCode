"""
https://leetcode-cn.com/problems/generate-parentheses/
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

        有效的括号组合:
            1.数量：( = )
            2.括号字符串组合 p
                对于任何 0 <= i < len(p) 都有：子串 p[0..i] 中左括号的数量都大于或等于右括号的数量。
                无论 i 在哪个位置; 恰好相等 如 ()() 还能补全 ()
        """
        ans = []
        path = ''

        def dfs(s1, s2):  # 左右括号使用数量
            nonlocal path
            if s1 + s2 == n * 2:
                ans.append(path)
                return

                # 使用 (
            if s1 < n:
                path += '('
                dfs(s1 + 1, s2)  # 当 3,0 return (递归的函数都执行完了)，进入 (( 的 s2 项
                path = path[:-1]

            # 使用 ) 此时必满足 ( 数量 > )
            if s2 < n and s1 > s2:
                path += ')'
                dfs(s1, s2 + 1)
                path = path[:-1]

        dfs(0, 0)
        return ans


s = Solution()
print(s.generateParenthesis(3))
