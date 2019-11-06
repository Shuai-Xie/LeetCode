# 错误解，想 1 次遍历完
def lengthOfLongestSubstring_error(s):
    ll = 0  # 初始化 ll 可能长度，may have empty str
    ll_str = ''
    i = 0
    while i < len(s):  # 用 for 里面更新 i 这里不会更新
        sub_str = s[i]
        while i + 1 < len(s) and s[i + 1] not in sub_str:
            sub_str += s[i + 1]
            i += 1
        # find a local max
        if len(sub_str) > ll:
            ll = len(sub_str)
            ll_str = sub_str
        i += 1  # 要开始下一轮，因为 s[i + 1] 与 sub_str 有重复字符
    return ll, ll_str


# 滑动窗口法
def lengthOfLongestSubstring1(s):
    ll = 0  # 初始化 ll 可能长度，may have empty str
    for i in range(len(s)):
        sub_str = s[i]
        while i + 1 < len(s) and s[i + 1] not in sub_str:
            sub_str += s[i + 1]
            i += 1
        # find a local max
        ll = max(len(sub_str), ll)
    return ll


# 滑动窗口
# 查找用的 sub_str 可用 hashset， python 查找效率: set > dict > list
def lengthOfLongestSubstring0(s):
    ll = 0  # 初始化 ll 可能长度，may have empty str
    for i in range(len(s)):
        sub_str = {s[i]}  # set
        while i + 1 < len(s) and s[i + 1] not in sub_str:
            sub_str.add(s[i + 1])
            i += 1
        # find a local max
        ll = max(len(sub_str), ll)
    return ll


# 优化的滑动窗口
def lengthOfLongestSubstring(s):
    st = {}
    i, ans = 0, 0
    for j in range(len(s)):
        if s[j] in st:
            i = max(i, st[s[j]])  # 更新后的起始位置 j+1
        ans = max(ans, j - i + 1)
        st[s[j]] = j + 1  # 字典后来值 更新前值的原理，能向前看找到一个最近的重复值所在位置的下一位
    return ans


print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring('dvdf'))
