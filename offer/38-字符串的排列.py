"""
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
"""

from typing import List


class Solution:
    """
    字符串的全排列 1 <= s 的长度 <= 8
    注意：如果字符串本身有重复 char，会造成 重排后，存在重复项；全排列时要剪枝

    全排列的排布，顺时针旋转90度，就是一颗树；DFS 路径遍历 + 重复节点剪枝
    """

    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []  # s 转 char list

        def dfs(x):
            # x: 当前元素位，也对应树的层数
            if x == len(c) - 1:
                res.append(''.join(c))  # 添加排列方案，c 是不断更新的
                return
            charset = set()

            for i in range(x, len(c)):
                if c[i] in charset:  # 重复，剪枝
                    continue

                charset.add(c[i])  # 下轮剪枝使用

                # 处理剩下情况
                c[i], c[x] = c[x], c[i]  # 交换, [x, len(c)-1] 范围内 任意一个 char 都可以在 x 位
                # 确定 c[x]，继续处理 x+1 之后的树的可能情况
                dfs(x + 1)
                # 恢复 c，继续 34 line 的不同确定值
                c[i], c[x] = c[x], c[i]

        dfs(0)
        return res


s = Solution()
print(s.permutation('abb'))
