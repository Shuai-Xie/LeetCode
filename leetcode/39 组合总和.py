"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。
"""

from typing import List


class Solution:
    # 都是正整数
    # 凑零钱 和为 sum
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        f = [[] for _ in range(target + 1)]  # 存方案

        for c in candidates:
            for t in range(c, target + 1):
                if f[t - c]:  # 已有方案
                    f[t] += [li + [c] for li in f[t - c]]
                else:
                    if t == c:
                        f[t].append([c])

        return f[-1]


s = Solution()
# candidates = [2, 3, 6, 7]
# target = 7
candidates = [2, 3, 5]
target = 8
print(s.combinationSum(candidates, target))
