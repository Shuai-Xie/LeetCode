"""
https://www.javazhiyin.com/48867.html
"""

import collections

strs = ["4PGC938", "2IYE230", "3CIO720", "1ICK750", "1OHV845"]


# 将字符串 按照倒数第1个字符进行分组 排序
def LSD(strs):
    W = len(strs[0])  # 字符串宽度
    R = 256  # ASCII 码总数量
    tmp = [''] * W

    for d in range(W - 1, -1, -1):

        # 统计每个字符出现频率
        cnt = [0] * (R + 1)  # 留出 0
        for s in strs:
            # char 对应的 ascii 码；使用 +1 后索引,计数此字符出现次数
            cnt[ord(s[d]) + 1] += 1

        # 频率 转为 元素起始位置的索引
        for r in range(R):
            cnt[r + 1] += cnt[r]

        # 对字符串元素 分组
        for s in strs:  # 存储起始位置
            idx = cnt[ord(s[d])]
            tmp[idx] = s


stus = [
    ('A', 1), ('B', 3), ('C', 1), ('D', 2), ('E', 3)  # 将数组按照 key=t[1] 分组
]

max_val = max([t[1] for t in stus])
cnt = [0] * (max_val + 2)  # 使用 cnt[n+1] 表示键值为 n 的 str 个数; 所以 max_val+2

# 统计键值频数
for s in stus:
    cnt[s[1] + 1] += 1
print(cnt)

# 将频数转成索引
for i in range(max_val + 1):
    cnt[i + 1] += cnt[i]
print(cnt)
