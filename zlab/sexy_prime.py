import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
if is_prime(n) and is_prime(n - 6):
    print('Yes')
    print(n - 6, end='')
elif is_prime(n) and is_prime(n + 6):
    print('Yes')
    print(n, end='')
else:
    print('No')
    while not (is_prime(n) and is_prime(n - 6)) or not is_prime(n) and is_prime(n + 6):
        n += 1
        print(n, end='')
