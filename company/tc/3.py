for n in range(2, 100):
    a1 = n
    res = a1
    res = int(res % (1e9 + 7))

    # 和公式 2^(n-1) * n
    for i in range(2, n + 1):  # 选出人的数目
        # 选出人数的递推公式
        a2 = a1 * (n - i + 1) // (i - 1)
        res += a2
        res = int(res % (1e9 + 7))
        a1 = a2

    print(n, res % (1e9 + 7), 2 ** (n - 1) * n % (1e9 + 7))
