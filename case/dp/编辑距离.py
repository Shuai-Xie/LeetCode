"""
编辑距离:
horse -> ros
可行操作: 增, 删, 替换; 问 变换到另一个 str 的最小操作次数

从 s -> t
两个字符串，二维 dp

例:
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = '#' + word1
        word2 = '#' + word2
        m, n = len(word1), len(word2)

        f = [[0] * n for _ in range(m)]
        # 初始化状态 只有 [0,0] 是对的，左,下 两条边界的值并不是真实情况, 在下面 for 中处理
        # f[i][j]: 子串 word1[:1], word2[:j] 之间的编辑距离

        for i in range(m):
            for j in range(n):
                # 初始化状态 要处理其中1个子串为空时的编辑距离
                if i == 0:
                    f[i][j] = j  # 操作 j 次添加
                elif j == 0:
                    f[i][j] = i  # 操作 i 次删除
                else:
                    if word1[i] == word2[j]:  # char 相等，不需要编辑
                        f[i][j] = f[i - 1][j - 1]
                    else:
                        # 注意 i,j 可以是两串各自的任意位置，所有不等情况下的处理
                        f[i][j] = min(
                            f[i - 1][j],  # s1 删除 i, (i-1,j) 编辑距离已知
                            f[i][j - 1],  # s1 新增 j, (i,j-1) 编辑距离已知
                            f[i - 1][j - 1],  # s1 替换 i->j, (i-1,j-1) 编辑距离已知
                        ) + 1

        return f[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance('horse', 'ros'))
    print(s.minDistance('intention', 'execution'))
