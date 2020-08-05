"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
"""


class Solution:
    # O(n)
    def firstUniqChar(self, s: str) -> str:
        cnt = {}
        for i, c in enumerate(s):
            if c in cnt:  # 出现多次
                cnt[c] = -1
            else:
                cnt[c] = i

        reverse_cnt = {v: k for k, v in cnt.items() if v >= 0}
        if len(reverse_cnt) > 0:
            return reverse_cnt[min(reverse_cnt.keys())]
        else:
            return ' '


s = Solution()
print(s.firstUniqChar("abaccdeff"))
print(s.firstUniqChar("aabb"))
print(s.firstUniqChar(""))
