"""
点到直线距离 https://blog.csdn.net/sinat_29957455/article/details/107490561
"""

a = (0, 10)
line = [[1, 0], [2, 0]]


def pt2line(pt, line_pts):
    """两点式"""
    x0, y0 = pt

    x1, y1 = line_pts[0]
    x2, y2 = line_pts[1]

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    d = abs(A * x0 + B * y0 + C) / (A ** 2 + B ** 2) ** 0.5
    return d


print(pt2line(a, line))
