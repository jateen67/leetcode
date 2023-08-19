def removeStars(s):
    stack = []

    for c in s:
        if c == "*":
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack)


print(removeStars("leet**cod*e"))

# time complexity: o(n)
# space complxity: o(n)
