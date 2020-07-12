def read_pkgs(txt):
    with open(txt) as f:
        c = f.readlines()
        pkgs = [l.split(' ')[0] for l in c]
        return pkgs


a_pkgs = read_pkgs('a.txt')
print(a_pkgs)
b_pkgs = read_pkgs('b.txt')

# 查看 b 中缺少的 a 库
for a in a_pkgs:
    if a not in b_pkgs:
        print(a)
