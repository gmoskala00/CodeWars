def dbl_linear(n):
    a = [1]
    b = [1]
    current = 0
    for _ in range(n):
        current = min(a[0], b[0])

        if current == a[0]:
            del a[0]
        if current == b[0]:
            del b[0]

        a.append(2 * current + 1)
        b.append(3 * current + 1)
    return min(a[0], b[0])