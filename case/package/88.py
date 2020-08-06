def show(a):
    a += 10
    print(a)


a = 100
show(a)
print(a)


def show2(a):
    a = a[:]
    a.append(10)
    print(a)


a = [1, 2, 3]
show2(a)
print(a)
