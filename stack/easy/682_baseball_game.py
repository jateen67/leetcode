def calPoints(operations):
    stack = []

    for i in range(len(operations)):
        if operations[i] == "+":
            stack.append(stack[-1] + stack[-2])
        elif operations[i] == "C":
            stack.pop()
        elif operations[i] == "D":
            stack.append(stack[-1] * 2)
        else:
            stack.append(int(operations[i]))

    return sum(stack)


print(calPoints(["5", "2", "C", "D", "+"]))

# time complexity: o(n)
# space complexity: o(n)
