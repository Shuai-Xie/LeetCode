T = int(input())


# A,B 确定函数; C,D 确定边界
def jifen(A, B, C, D):
    def f(x):
        return A / 3 * x ** 3 + x ** 2 / 2 + B * x

    return f(D) - f(C)


res = []
for i in range(T):
    A, B, C, D = map(int, input().split())
    res.append(jifen(A, B, C, D))

for i in range(T):
    print(res[i])
