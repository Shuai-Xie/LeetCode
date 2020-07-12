class Solution:
    def cuttingRope(self, n: int) -> int:
        def mul_arr(arr):
            import functools
            return functools.reduce(lambda x, y: x * y, arr)

        def cut_m_arr(m):
            """均分原则
            当确定为 m 段时，各段的最佳划分，边长相等时，算术几何不等式
            :param m: 划分段数
            :return:
            """
            base, remain = n // m, n % m  # 基数，余数
            if remain > base / 2:  # 余数偏大，分给基数
                base += 1
            last_num = n - base * (m - 1)
            k = [base] * (m - 1) + [last_num]
            return k

        def brute_force(n):
            max_product = 1
            max_arr = None
            for m in range(2, n):  # 肯定不会是 n 段，那样积 =1
                if mul_arr(cut_m_arr(m)) > max_product:
                    k = cut_m_arr(m)
                    max_product = mul_arr(k)
                    max_arr = k
            print(max_product, max_arr)
            return max_product

        def math_force(n):
            """
            求 (x)^(n/x) 取极大值时，x 的取值
            """
            import math
            if n <= 3:  # 2,3 -> 1*1, 2*1
                return n - 1
            else:  # 每段长为 3 最优
                a, b = n // 3, n % 3
                if b < 3 / 2:  # 小于一半，加到最后1个数，总共 a 个数 [实际上 使用 3+b 得到的 arr 是不对的，[4] vs. [2,2]]
                    return int(math.pow(3, a - 1) * (3 + b))  # note: 注意返回整型
                else:  # 过半，新数，总共 a+1 个数
                    return int(math.pow(3, a) * b)

        res = brute_force(n)
        res = math_force(n)

        return res


def demo_func():
    import numpy as np
    import matplotlib.pyplot as plt

    xs = np.arange(1, 100) / 10

    for n in [6, 8, 10]:
        ys = [x ** (n / x) for x in xs]
        plt.plot(xs, ys, label=f'n={n}')

    plt.legend()
    plt.title(r'$y=x^{\frac{n}{x}}$')
    plt.show()


demo_func()
# s = Solution()
# s.cuttingRope(4)
