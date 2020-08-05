"""
给定一个数字，我们按照如下规则把它翻译为字符串：
26个英文字母 与 数字对应
0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

有点 信号解码 感觉

链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
"""


class Solution:

    def translateNum(self, num: int) -> int:

        # DP 往往从 最后的情况 考虑
        num_str = str(num)
        num_len = len(num_str)

        if num_len == 1:
            return 1

        dp = [1, 1]  # num_len = 0,1, 注意 len=0 也是一种情况
        for i in range(2, num_len + 1):
            # 后两位数字
            val = int(num_str[i - 2:i])
            if 10 <= val <= 25:  # 可整, 可分
                dp.append(dp[i - 2] + dp[i - 1])
            else:  # 整体无对用char，只能分，分后最后1个数 只有1种情况 与 dp[i-1] 结果一致
                dp.append(dp[i - 1])
        return dp[-1]

    def translateNum_result(self, num: int):  # 得到所有可能情况，注意：只用保留 n-2,n-1 的情况
        # chr(v): v -> char, type is str
        map_dict = {str(i): chr(v) for i, v in enumerate(range(97, 123))}

        # DP 往往从 最后的情况 考虑
        num_str = str(num)
        num_len = len(num_str)

        if num_len == 1:
            return [map_dict[num_str]]

        dp = [1, 1]  # num_len = 0,1, 注意 len=0 也是一种情况
        res_n_2 = ['']  # n-2 情况
        res_n_1 = [map_dict[num_str[0]]]  # n-1 结果

        for i in range(2, num_len + 1):
            # 后两位数字
            c1, c2 = num_str[i - 2], num_str[i - 1]  # 末尾两个 char
            val = int(c1 + c2)  # 末尾 两位数
            if 10 <= val <= 25:  # 可整, 可分
                dp.append(dp[i - 2] + dp[i - 1])
                # 整 + 分[只在 res_n_1 中加最后1个]
                tmp = [v + map_dict[c1 + c2] for v in res_n_2] + [v + map_dict[c2] for v in res_n_1]
                res_n_1, res_n_2 = tmp, res_n_1
            else:  # 整体无对用char，只能分，分后最后1个数 只有1种情况 与 dp[i-1] 结果一致
                dp.append(dp[i - 1])
                tmp = [v + map_dict[c2] for v in res_n_1]
                res_n_1, res_n_2 = tmp, res_n_1

        return res_n_1


s = Solution()
print(s.translateNum(12258))
print(s.translateNum_result(12258))
print(s.translateNum(506))
print(s.translateNum_result(506))
