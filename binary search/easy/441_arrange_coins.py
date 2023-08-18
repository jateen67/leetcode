import math


def arrangeCoins(n):
    # res = 0
    # level = 0

    # while True:
    #     level += 1
    #     n -= level
    #     if n == 0:
    #         return level
    #     if n <= 0:
    #         return level - 1
    return int((-1 + math.sqrt(1 + (8 * n))) / 2)


print(arrangeCoins(5))

# time complexity: o(1)
# space complexity: o(1)
