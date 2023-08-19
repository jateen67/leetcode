def validateStackSequences(pushed, popped):
    stack = []
    r = 0

    for l in range(len(pushed)):
        stack.append(pushed[l])
        while stack and stack[-1] == popped[r]:
            stack.pop()
            r += 1

    return not stack


print(validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))

# time complexoty: o(n)
# space complexity: o(n)
