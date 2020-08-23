"""
输入一个只由 0 1 组成的长字符串
如：0000111110000
计算 使 0,1 个数相等的 最长子串
"""


def longest_01substr(s):
    sum_pos = {0: -1}  # 初始位置 -1，和为 0
    len_ = 0
    sum_ = 0
    for i in range(len(s)):
        if s[i] == '0':
            sum_ -= 1
        elif s[i] == '1':
            sum_ += 1
        if sum_ not in sum_pos:  # 只需要记录 sum 第一次出现的位置即可
            sum_pos[sum_] = i
        else:
            len_ = max(len_, i - sum_pos[sum_])
    return len_


def longest_012substr_old(s):
    sum01_pos, sum02_pos = {}, {}
    sum01, sum02 = 0, 0
    len01, len02 = 0, 0
    res = 0

    for i in range(len(s)):
        if s[i] == '0':
            sum01 -= 1
            sum02 -= 1
        elif s[i] == '1':
            sum01 += 1
        elif s[i] == '2':
            sum02 += 1

        # 每个 i 状态 都记录两个值 sum01/sum02
        if sum01 not in sum01_pos:
            sum01_pos[sum01] = i
        else:
            len01 = i - sum01_pos[sum01] + 1

        if sum02 not in sum02_pos:
            sum02_pos[sum02] = i
        else:
            len02 = i - sum02_pos[sum02] + 1

        res = max(res, min(len01, len02))

    return res


def longest_012substr(s):
    n = len(s)
    # 数组 index 表示差值；value 表示位置
    pre01 = [-1] * (2 * n + 1)
    pre02 = [-1] * (2 * n + 1)
    cnts = {str(i): 0 for i in range(3)}

    res = 0
    for i in range(len(s)):
        # 长度 初始化
        len01, len02 = -1, -1
        cnts[s[i]] += 1

        diff01 = cnts['0'] - cnts['1']
        diff02 = cnts['0'] - cnts['2']

        if pre01[diff01 + n] == -1:
            pre01[diff01 + n] = i  # 差值为 diff01 的 位置
        else:
            len01 = i - pre01[diff01 + n]

        if pre02[diff02 + n] == -1:
            pre02[diff02 + n] = i
        else:
            len02 = i - pre02[diff02 + n]

        if len01 != -1 and len02 != -1:
            res = max(res, min(len01, len02))

    return res


def longest_01substr_iter(s):
    len_ = 0
    for i in range(len(s)):  # 子串起始位置
        cnt = {'0': 0, '1': 0}
        for j in range(i, len(s)):  # 长度范围，剩下子串
            cnt[s[j]] += 1
            if cnt['0'] == cnt['1']:  # 子串相等了
                len_ = max(len_, j - i + 1)
    return len_


def longest_012substr_iter(s):
    len_ = 0
    # O(n^2)
    for i in range(len(s)):  # 子串起始位置
        cnt = {'0': 0, '1': 0, '2': 0}
        for j in range(i, len(s)):  # 长度范围，剩下子串
            cnt[s[j]] += 1
            if cnt['0'] == cnt['1'] == cnt['2']:  # 子串相等了
                len_ = max(len_, j - i + 1)
    return len_


def longest_any_substr_iter(s, num_chars=2):
    len_ = 0
    for i in range(len(s)):  # 子串起始位置
        cnt = [0] * num_chars
        for j in range(i, len(s)):  # 长度范围，剩下子串
            cnt[int(s[j])] += 1
            if equal_arr(cnt):  # 子串相等了
                len_ = max(len_, j - i + 1)
    return len_


def equal_arr(arr):  # 判断 arr 中数字都相同
    for i in range(1, len(arr)):
        if arr[i] != arr[0]:
            return False
    return True


if __name__ == '__main__':
    s1 = '012'
    # s1 = '0201111000222'
    s2 = '2001111000222'
    s3 = '2001111000222000111222'
    print(longest_012substr_iter(s1), longest_012substr(s1))
    print(longest_012substr_iter(s2), longest_012substr(s2))
    print(longest_012substr_iter(s3), longest_012substr(s3))
    # print(longest_any_substr_iter(s2, num_chars=3))
    # print(longest_any_substr(s2, chars=['0', '1', '2']))
