"""
https://cloud.tencent.com/developer/article/1167159

python 基本数据类型 https://www.cnblogs.com/snaildev/p/7544558.html
- Number, String, List, Tuple, Dictionary

Number 分为 4 种不同的
- int       有符号整型   64位机上 为 64bits, 9223372036854775807
- long      长整型         无限大，没有位宽；背后采用 list 存储数据，分别计算，再拼起来
- float     浮点型         类似 C double，64bits, 52位底数，11位指数，1个符号位 https://blog.csdn.net/m0_37829435/article/details/79611010
- complex   复数

有符/无符号数的最大值
8    127                    255
16   32767                  65535
32   2147483647             4294967295
64   9223372036854775807    18446744073709551615
"""

import sys


def see_max_number():
    for x in [8, 16, 32, 64]:
        print(2 ** (x - 1) - 1)

    print(float('inf'))  # 无限大的浮点数值
    # -2**63 - 2**63-1
    print(sys.maxsize)  # 最大整型 9223372036854775807 [64bits]

    a = sys.maxsize  # type 为 int，但默认 long 计算，没有 long 这个 class，只有 int
    b = a * a
    print(b)
    print(type(a), type(b))  # 虽然 type 为 int，实际为 long


# 使用数组存储的大数，从低位到高位
# 23 934 543
#    454 632
a = [543, 934, 23]
b = [632, 454]

# 实际二进制
# Pylong_SHIFT = 2 ** 15  # 每个 子片段最多 15 位，防止乘法运算溢出，因为32位机器 int 总共 32 bits
# Pylong_MASK = (1 << 15) - 1  # 15 1
# print(Pylong_MASK)
# print(bin(Pylong_MASK))  # 输出二进制
# print('{:b}'.format(Pylong_MASK))

# 移位 掩码
# 10进制 例子
Pylong_SHIFT = 1000
Pylong_MASK = 999


def recover_rand_shift_data(num_arr):
    cur_s = num_arr[0]  # 当前组合数字之和
    cur_l = len(str(num_arr[0]))
    for v in num_arr[1:]:  # 剩下数字
        cur_s += v * 10 ** cur_l  # note: 10** 别忘了
        cur_l += len(str(v))
    return cur_s


# c = [12, 1, 900, 12]
# print(recover_rand_shift_data(c))


def recover_fixed_shift_data(num_arr):
    s = 0
    for i, v in enumerate(num_arr):
        s += v * Pylong_SHIFT ** i
    return s


def long_norm(num_arr):
    """
    去掉多余的空间，调整数组的到正确的长度
    因为 加法 和 乘法 都提前估计了结果的 子片段个数，可能存在未使用完的情况
    eg: [176, 631, 0, 0]  ==>  [176, 631]
    """
    # 从倒数第1个遍历
    if num_arr[-1] != 0:  # 最后1个都不是0，直接返回
        return num_arr

    for i in range(1, len(num_arr)):
        if num_arr[-i] != 0:
            return num_arr[:-(i - 1)]


def x_add(a, b):
    size_a, size_b = len(a), len(b)
    carry = 0  # 进位

    # 假定 a 是二者 长度较大 的一方，方便 code
    if size_a < size_b:  # swap
        size_a, size_b = size_b, size_a
        a, b = b, a

    # 保存结果的数组，加法 最多进位长度 1 个
    z = [0] * (size_a + 1)
    i = 0  # 遍历各个 子片段数据

    # a,b 数据是从 低位到高位存储的
    # 所以遍历 i，符合竖式计算方式
    while i < size_b:  # 较小的数的位数
        carry += a[i] + b[i]  # +=，向高位计算时，要保留低位的 carry
        carry, z[i] = carry // Pylong_SHIFT, carry % Pylong_SHIFT  # 进位 余数
        i += 1

    while i < size_a:
        carry += a[i]  # 此时相当于 b[i]=0
        carry, z[i] = carry // Pylong_SHIFT, carry % Pylong_SHIFT  # 进位 余数
        i += 1

    z = long_norm(z)

    return z


def x_mul(a, b):
    size_a, size_b = len(a), len(b)

    z = [0] * (size_a + size_b)  # 两数相乘 积的位数不超过 位数之和

    for i in range(size_b):
        carry = 0

        tmp = [0] * (size_a + size_b)  # 临时变量
        pz = i  # note: 记录 乘积子段 的起始位置，对应位置加和
        for j in range(size_a):
            carry += b[i] * a[j]  # 乘积进位，note: 之前定义字段最多15位，就是保证乘积仍在 int 范围内
            carry, tmp[pz] = carry // Pylong_SHIFT, carry % Pylong_SHIFT
            pz += 1

        if carry:  # 乘完后 还有进位
            carry += tmp[pz]
            carry, tmp[pz] = carry // Pylong_SHIFT, carry % Pylong_SHIFT
            pz += 1

        if carry:
            tmp[pz] += carry % Pylong_SHIFT

        # a 乘完 b 的子片段后，与 z 做加和
        tmp = long_norm(tmp)
        # print(tmp)  # 数字头部的 0 去掉，而尾部要保留
        z = x_add(z, tmp)

    return z


def demo():
    # 恢复原数后验证
    _a = recover_fixed_shift_data(a)
    _b = recover_fixed_shift_data(b)
    print(_a)
    print(_b)
    # add
    print(_a + _b)
    print(recover_fixed_shift_data(x_add(a, b)))
    # mul
    print(_a * _b)
    print(recover_fixed_shift_data(x_mul(a, b)))


demo()
