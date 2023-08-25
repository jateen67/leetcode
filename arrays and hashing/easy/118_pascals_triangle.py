def generate(numRows):
    res = [[1]]

    for i in range(numRows - 1):
        level = [0] + res[-1] + [0]
        new_level = []
        for j in range(1, len(level)):
            new_level.append(level[j] + level[j - 1])
        res.append(new_level)

    return res


print(generate(5))

# time complexity: o(n^2)
# space complexity: o(n^2)
