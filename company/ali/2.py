# A = x+y
# B = xy
A, B = 4, 4
n = 3
mod = 1e9 + 7


# (xy)^n
def pow_xy_n(n):
    if n == 1:
        return B
    r = n % 2
    res = pow_xy_n(n // 2)

    if r == 0:
        return res * res % mod
    else:
        return res * res * B % mod


memo = {
    1: A,  # x+y
    2: A * A - 2 * B  # (x+y)^2 - 2xy
}


# x^n + y^n
def pow_xn_yn(n):  # x
    if n in memo:
        return memo[n]

    # 二分
    r = n % 2
    sum_half_n = pow_xn_yn(n // 2)
    mul_half_n = pow_xy_n(n // 2)

    # x
    half_n = (sum_half_n * sum_half_n - 2 * mul_half_n) % mod
    print(n, half_n)

    res = half_n % mod if r == 0 else (half_n * A - pow_xn_yn(n - 2) * B) % mod
    memo[n] = res
    return res


print(pow_xn_yn(n))
