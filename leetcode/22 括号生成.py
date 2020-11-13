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
        def dfs(i=0, s1=0, s2=0):
            """
            :param i: 当前所在 str 的 idx
            :param s1: 左括号个数
            :param s2: 右括号个数
            :return:
            """
            nonlocal ans
            if i == n * 2:  # 到末尾了
                res.append(ans)

            if s1 < n:  # 还可以添加左括号
                ans += '('
                s1 += 1
                dfs(i + 1, s1, s2)
                ans = ans[:-1]  # 回溯
                s1 -= 1

            if s2 < n and s1 > s2:  # ')' 不能单独出现; （ 一定比 ) 个数多时，才可添加
                ans += ')'
                s2 += 1
                dfs(i + 1, s1, s2)
                ans = ans[:-1]
                s2 -= 1

        dfs()
        return res

    def generateParenthesis2(self, n: int) -> List[str]:
        res = []
        ans = ''

        # 回溯法，根据 ( 使用次数，判断 ) 是否添加
        def dfs(i, s1, s2):
            nonlocal ans
            if i == n * 2:  # 长度达到
                res.append(ans)
                return

            if s1 < n:
                ans += '('  # 使用左括号
                s1 += 1
                dfs(i + 1, s1, s2)  # 最终情况是 s1=3
                ans = ans[:-1]  # 回溯去掉最新添加的 (
                s1 -= 1

            if s2 < n and s1 > s2:  # ( 比 ) 多才会补充 )
                ans += ')'
                s2 += 1
                dfs(i + 1, s1, s2)
                ans = ans[:-1]
                s2 -= 1


s = Solution()
print(s.generateParenthesis(3))
