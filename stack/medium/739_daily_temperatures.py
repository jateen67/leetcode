def daily(temperatures):
    stack = []
    res = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and stack[-1][0] < temperatures[i]:
            temp, idx = stack.pop()
            res[idx] = i - idx
        stack.append((temperatures[i], i))

    return res


print(daily([73, 74, 75, 71, 69, 72, 76, 73]))

# time complexoty: o(n)
# space complexity: o(n)
