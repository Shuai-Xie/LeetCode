# 试除法
def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):  # 平方根更小
        if x % i == 0:
            return False
    return True


# 试除法浪费了很多时间 在 明显就是合数的数上面
def generate_primes(n=20):
    return [x for x in range(2, n + 1) if is_prime(x)]


# 埃拉托色尼筛
def eratosthenes_primes(n=100):
    """
    1.创建连续数表 [2,..,n]
    2.p=2 ~ √n 素数，枚举 2p,3p，将素数的倍数筛掉
    改进：
        能被质因数分解的素数 会被多次标记；如 15 = 3*5, 会被 3/5 标记
        将 2 的枚举起点从 p**2 开始;
            质因数分解的性质: 比 p**2 小的数，都存在比 p 更小的质因数；
            只是优化了起始位置，p**2 之后也有很多能被 <p 质数的倍数，但是没过滤
    """
    isprime = [True] * (n + 1)  # 使用 flag 避免繁杂的 存取操作

    for i in range(2, int(n ** 0.5) + 1):
        if isprime[i]:  # 素数，开筛
            for j in range(i * i, n + 1, i):  # 起点很有意思
                isprime[j] = False

    return [i for i in range(2, n + 1) if isprime[i]]


def get_div_primes(n=20):
    # 过滤掉 空 list
    return {
        x: [x] if is_prime(x) else [i for i in generate_primes(x // 2) if x % i == 0] for x in range(2, n + 1)
    }


import functools
import time


def cal_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)  # 有返回值的装饰器函数
        t2 = time.time()
        print('time:', t2 - t1)
        return res

    return wrapper  # 返回包装后的函数


@cal_time
def factor(n):  # 质因数分解
    if is_prime(n):
        return [n]

    res = []
    # n = 54546466466
    # primes = generate_primes(int(n ** 0.5) + 1)  # 0.5359675884246826
    primes = eratosthenes_primes(int(n ** 0.5) + 1)  # 0.027966976165771484
    while not is_prime(n):
        for p in primes:
            if n % p == 0:
                res.append(p)
                n //= p
                break
    res.append(n)  # 添加最后一个值
    return res


# print(generate_primes())
# print(eratosthenes_primes())
print(factor(54546466466))
