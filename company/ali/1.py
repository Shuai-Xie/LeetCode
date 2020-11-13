# 数组组数
# t = int(input())

# 交换 a 中 2个字符 or 不交换
# 使得 a > b
# 若可以，输出交换 a; 否则输出 b


a = 'aabb'
b = 'abab'

alen = len(a)
blen = len(b)

c_len = min(alen, blen)  # 二者可比较的长度

