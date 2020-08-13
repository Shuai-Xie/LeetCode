"""
n 个物品，各自都有价值，分给两个人
问：当分给两个人的价值最大时，最终剩余多少
"""

from typing import List


class Solution:
    # dfs 回溯: 回到之前状态的意思
    def avg_remain(self, nums: List[int]) -> int:
        n = len(nums)
        use = [0] * n
        ans = 0

        # 只是遍历了所有状态，树遍历结束时，函数内变量并未保存中间结果, 只有外部 global 才可
        def dfs(i, s1, s2):  # 第i个元素
            nonlocal ans  # note: 函数内部 修改 外部变量
            if i == n:  # 终了
                return
            for s in range(3):  # 递归树 每个节点有3种选择状态
                # 选一状态
                use[i] = s
                if s == 1:
                    s1 += nums[i]
                elif s == 2:
                    s2 += nums[i]
                # 比较 更新值
                if s1 == s2:
                    ans = max(ans, s1)
                # 深入结点
                dfs(i + 1, s1, s2)
                # 回溯下一状态
                use[i] = 0
                if s == 1:
                    s1 -= nums[i]
                elif s == 2:
                    s2 -= nums[i]

        dfs(0, 0, 0)
        return sum(nums) - 2 * ans


nums = [30, 60, 5, 15, 30]
s = Solution()
print(s.avg_remain(nums))
