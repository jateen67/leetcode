def climb(n):
    a = 0
    b = 1
    c = 0

    if n == 1:
        return 1

    for i in range(n):
        c = a + b
        a = b
        b = c

    return c


print(climb(5))

# time complexity: o(n)
# space complexity: o(1)
