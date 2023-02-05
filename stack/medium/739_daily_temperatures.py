def daily(temps):
    res = [0] * len(temps)
    stack = []

    for i in range(len(temps)):
        while stack and temps[i] > stack[-1][0]:
            popped = stack.pop()
            idx = popped[1]
            res[idx] = i - idx
        stack.append((temps[i], i))

    return res


print(daily([73, 74, 75, 71, 69, 72, 76, 73]))

# time complexoty: o(n)
# space complexity: o(n)
