def twoSum(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1

    while True:
        added = numbers[p1] + numbers[p2]
        if added < target:
            p1 += 1
        elif added > target:
            p2 -= 1
        else:
            return [p1 + 1, p2 + 1]


print(twoSum([2, 7, 11, 15], 9))

# time complexity: o(n)
# space complexity: o(1)
