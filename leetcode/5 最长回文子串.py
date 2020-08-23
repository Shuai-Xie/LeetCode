# 误解1
# 反转 S 得到 S'，再求二者的最长公共子串，但是反转后，公共字串不一定回文
# 只要分割点存在 >1 个不同，回文两侧就会断开，变成单段重复，而不是回文
# S  = 'abacdfgdcaba'
# S' = 'abacdgfdcaba'
# 即 S 的其他部分如果存在 非回文字串的反向副本时，求 (S,S') 的算法就会失败
# 所以，每当找到公共子串候选项时，都要先判断 S_idx 和 S'_idx_inverse 是否相同
# 判断定位到 同一子串后，再判断是否回文

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        def get_max_len(left, right):
            while left >= 0 and right < n and s[left] == s[right]:  # 满足回文
                left -= 1
                right += 1
            return right - left - 1  # 跳出时 左右相当于各自多走1步，要用 (right-1) - (left+1) +1 才表示真正位置

        max_len, max_i = 0, -1
        for i in range(n):  # 'bb' 要让 idx 从 0 开始
            odd_len = get_max_len(i, i)
            even_len = get_max_len(i, i + 1)
            len_i = max(odd_len, even_len)
            if len_i > max_len:
                max_len = len_i
                max_i = i

        half, remain = max_len // 2, max_len % 2
        if remain == 0:  # 偶数
            return s[max_i - half + 1: max_i + half + 1]
        else:
            return s[max_i - half:max_i + half + 1]

    def longestPalindrome_dp(self, s: str) -> str:
        

s = Solution()
print(s.longestPalindrome('bb'))
print(s.longestPalindrome('babad'))
print(s.longestPalindrome('abacdfgdcaba'))
