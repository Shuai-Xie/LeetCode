a = ["12", "787", 1212, 12, "2323", "100", 7762]


def sort_arr(a):
    return sorted([v for v in a if isinstance(v, int)])


print(sort_arr(a))
