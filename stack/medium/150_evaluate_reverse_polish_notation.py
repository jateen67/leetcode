def evalRPN(tokens):
    stack = []

    for t in tokens:
        if t == "+":
            x, y = stack.pop(), stack.pop()
            stack.append(x + y)
        elif t == "-":
            x, y = stack.pop(), stack.pop()
            stack.append(y - x)
        elif t == "*":
            x, y = stack.pop(), stack.pop()
            stack.append(x * y)
        elif t == "/":
            x, y = stack.pop(), stack.pop()
            stack.append(int(y / x))
        else:
            stack.append(int(t))

    return stack[0]


print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

# time complexoty: o(n)
# space complexity: o(n)
