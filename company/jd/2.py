N, M = map(int, input().split())


def replace_zero(s):  # 去掉首位的 0
    while len(s) > 0 and s[0] == '0':
        s = s[1:]
    return s


def is_huiwen(s):
    cut = len(s) // 2
    if len(s) % 2 == 1:
        left, right = s[:cut + 1], s[cut:][::-1]
    else:
        left, right = s[:cut], s[cut:][::-1]

    left, right = replace_zero(left), replace_zero(right)
    return left == right


def is_su(n):
    if n == 1 or n == 2:
        return True
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def is_huiwensu(n):
    if n == 1:
        return True

    if n < 10:
        return is_su(n)

    else:
        s = str(n)

        for i in range(len(s)):
            ss = s[:i] + s[i + 1:]
            if is_huiwen(ss) and is_su(int(ss)):
                return True

        return False


# 如果去掉位数 是 末尾
cnt = 0
while N <= M:



for i in range(N, M + 1):
    if is_huiwensu(i):
        cnt += 1
print(cnt)
