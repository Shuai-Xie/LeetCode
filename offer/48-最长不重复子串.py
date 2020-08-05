"""
最长的不包含重复字符的子字符串

判断 字符串 是否包含重复字符
- 排序，相邻比较, O(nlog(n))
- 哈希表，存储计数 > 1, O(n)
"""


class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        # 滑动窗口法，保证窗口内 s 不重复
        res = 0
        i = 0  # head
        pos = {}

        for j in range(len(s)):  # 窗口右侧 始终向右，只用移动左侧
            if s[j] in pos:
                # i j 之间始终表示不重复的 char
                # pos[s[j] 存在 > i 可能，这样 ij 维护的区间就不是 unique s
                # 如 "abba"，最后1个 a 时，i 已经在 pos[a] 之前了
                # i = pos[s[j]] + 1
                i = max(i, pos[s[j]] + 1)
            res = max(res, j - i + 1)
            pos[s[j]] = j

        return res

    # 保存 结果
    def lengthOfLongestSubstring(self, s: str):
        substrs = []

        res = 0
        i = 0  # head
        pos = {}

        for j in range(len(s)):  # 窗口右侧 始终向右，只用移动左侧
            if s[j] in pos:
                i = max(i, pos[s[j]] + 1)

            if j - i + 1 > res:  # 更新重来
                substrs = [s[i:j + 1]]
                res = j - i + 1
            elif j - i + 1 == res:  # 增加同样长度 substr
                substrs.append(s[i:j + 1])

            pos[s[j]] = j

        # 要去重，set 即可
        return substrs


s = Solution()
print(s.lengthOfLongestSubstring("abba"))  # 最后1个 a 时，
print(s.lengthOfLongestSubstring("p"))
print(s.lengthOfLongestSubstring('abcabcbb'))
print(s.lengthOfLongestSubstring('bbbbbb'))
print(s.lengthOfLongestSubstring("pwwkew"))
