"""
https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/
请实现一个函数用来匹配包含'. '和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的 所有字符匹配 整个模式。

例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

困难
编译原理，归约？
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """

        :param s:
        :param p: 包含'. '和'*'的正则表达式
        :return:
        """

