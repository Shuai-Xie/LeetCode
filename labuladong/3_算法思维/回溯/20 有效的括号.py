"""
https://leetcode-cn.com/problems/valid-parentheses/
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。

([)]
False
"""


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']  # 栈赋初值; ? 表示栈空状态，方便 pop 判断是否直接面对了出栈的右括号

        for c in s:
            if c in dic:
                stack.append(c)
            else:  # c 是右括号
                # 遇到右括号 而左括号不匹配 or 左边为空的状态
                if dic[stack.pop()] != c:  # 应该匹配的右括号 ！= c 当前访问的括号
                    return False
        return len(stack) == 1  # 正常情况

    def isValid_old(self, s: str) -> bool:
        stack = []
        for c in s:
            # 左括号入栈
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                # 出现了右括号，而栈为空
                if not stack:
                    return False
                else:
                    if c == ')' and stack[-1] == '(' or c == '}' and stack[-1] == '{' or c == ']' and stack[-1] == '[':
                        stack.pop()
                    else:  # 最深层没有找到匹配的左括号
                        return False

        return not stack  # 栈为空为 true


sovler = Solution()
# s = '([)]'
# s = '{()[([])]([])}'
s = ']()'
print(sovler.isValid(s))
print(sovler.isValid_old(s))
