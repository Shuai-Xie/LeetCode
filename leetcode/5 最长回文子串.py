# 误解1
# 反转 S 得到 S'，再求二者的最长公共子串，但是反转后，公共字串不一定回文
# 只要分割点存在 >1 个不同，回文两侧就会断开，变成单段重复，而不是回文
# S  = 'abacdfgdcaba'
# S' = 'abacdgfdcaba'
# 即 S 的其他部分如果存在 非回文字串的反向副本时，求 (S,S') 的算法就会失败
# 所以，每当找到公共子串候选项时，都要先判断 S_idx 和 S'_idx_inverse 是否相同
# 判断定位到 同一子串后，再判断是否回文


def longest_palindrome(s):
    # 中心两边扩展法
    def expand_around_center(left, right):
        # 以 left,right 为中心 idx 向两边扩展
        L, R = left, right
        # 合理范围内 向两边扩展 L,R
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1  # 跳出循环时，L,R 是不等的两个下表: (R-1) - (L+1) +1

    if len(s) < 1:
        return ''
    start, end = 0, 0  # idx 位置
    for i in range(len(s)):
        odd_len = expand_around_center(i, i)  # 奇数长度，左右起始 idx 相同; 执行 n 次
        even_len = expand_around_center(i, i + 1)  # 偶数长度，左右起始 idx 相差1; 执行 n-1 次
        max_len = max(odd_len, even_len)
        # 更新 子串起止点
        if max_len > end - start:
            start = i - (max_len - 1) // 2  # 下限 idx, 同时考虑 max_len 奇偶情况
            end = i + max_len // 2  # 上限 idx

    return s[start:end + 1]


print(longest_palindrome('babad'))
print(longest_palindrome('abacdfgdcaba'))
