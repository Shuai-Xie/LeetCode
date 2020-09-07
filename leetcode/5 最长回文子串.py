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
        # 以 i 为中心，分奇偶两种情况 从中间向两边扩展
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
        # 判断 i..j 是否为回文
        # dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
        # dp 判断 回文串; 首尾字母相等 并且内部是回文
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        # 对角线一定回文 初始化
        for i in range(size):
            dp[i][i] = True

        # 始终 i<j
        for j in range(1, size):  # 定右侧
            for i in range(0, j):  # 寻左侧
                if s[i] == s[j]:
                    if j - i < 3:  # 长度<=3, 直接可通过 s[i],s[j] 判断
                        dp[i][j] = True
                    else:  # 状态转移，判断内部是不是
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:  # 判断 寻找最长回文
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i

        return s[start:start + max_len]

    def longestPalindrome_bf(self, s: str) -> str:
        def get_plen(s):
            if s[::-1] == s:
                return len(s)
            else:
                return -1

        n = len(s)
        plen = -1
        pi = -1
        for i in range(n - 1):  # 左边界
            for j in range(i + 1, n):  # 右边界
                sub_len = get_plen(s[i:j + 1])
                if sub_len > plen:
                    plen = sub_len
                    pi = i

        return s[pi:pi + plen]


so = Solution()
# s = 'bb'
s = 'babad'
print(so.longestPalindrome(s))
print(so.longestPalindrome_bf(s))
