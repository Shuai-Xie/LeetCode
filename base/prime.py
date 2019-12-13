import math


def generate_primes_old(n=20):
    a = []
    for i in range(2, n + 1):  # 到 n
        j = 2
        max_div = int(math.sqrt(i)) + 1
        for j in range(2, max_div + 1):  # 上限到 sqrt 即可
            if i % j == 0:
                break
        if j == max_div:  # 只能被 1 和 自身整除
            a.append(i)
    print(a)


def generate_primes(n=20):
    # [] 中 x,i 都可，python 中空 list [] 相当于 False
    return list(filter(lambda x: not [x for i in range(2, x // 2 + 1) if x % i == 0], range(2, n + 1)))


def get_all_divisors(n=20):
    # 过滤掉 空 list
    return list(filter(lambda l: l, [[(x, i) for i in range(2, x // 2 + 1) if x % i == 0] for x in range(2, n + 1)]))
