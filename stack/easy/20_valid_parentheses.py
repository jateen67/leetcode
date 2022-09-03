def isValid(s):
    if len(s) % 2 == 1:
        return False

    v = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for i in range(len(s)):
        if s[i] in v:
            stack.append(s[i])
        else:
            if not stack:
                return False
            popped = stack.pop()
            if s[i] != v[popped]:
                return False
    return not stack


print(isValid('({[[]]})'))

# time complexity: o(n)
# space complexity: o(n)
