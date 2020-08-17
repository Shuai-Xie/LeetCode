"""
https://leetcode-cn.com/problems/combination-sum-ii/
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        path = []
        res = []

        def dfs(ta, begin):
            if ta == 0:
                res.append(path[:])
                return
            if ta < 0:
                return

            for i in range(begin, n):
                # i==begin 表示这个数是 第一次遇到，要使用
                # 递归到这里时，表示 包含 candidates[i - 1] 已经找到解或为空，不用再考虑
                if i > begin and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(ta - candidates[i], i + 1)  # 每个元素只能用1次，从前往后搜
                path.pop()

        dfs(target, 0)
        return res

    def combinationSum2_dp(self, candidates: List[int], target: int) -> List[List[int]]:
        # todo
        # candidates 中出现 重复元素
        # 每个数字只能用一次, 01 背包问题
        f = [[] for _ in range(target + 1)]
        n = len(candidates)
        candidates.sort()

        for i in range(len(candidates)):
            c = candidates[i]
            for j in range(target, c - 1, -1):
                if f[j - c]:
                    f[j] += [li + [c] for li in f[j - c]]
                else:
                    if c == j and [c] not in f[j]:  # 单个元素 作方案首位 只添加1次
                        f[j].append([c])

        return f[-1]


s = Solution()
# candidates = [10, 1, 2, 7, 6, 1, 5]
# target = 8
# print(s.combinationSum2(candidates, target))

candidates = [2, 5, 2, 1, 2]
for target in range(1, 6):
    print(target, s.combinationSum2(candidates, target))
    print(target, s.combinationSum2_dp(candidates, target))
