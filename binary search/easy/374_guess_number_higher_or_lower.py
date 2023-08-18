def guess(n, pick):
    if n == pick:
        return 0
    elif n > pick:
        return -1
    else:
        return 1


def guessNumber(n, pick):
    l, r = 0, n

    while l <= r:
        mid = (l + r) // 2

        if guess(mid, pick) == 0:
            return mid
        elif guess(mid, pick) == -1:
            r = mid - 1
        else:
            l = mid + 1


print(guessNumber(10, 6))

# time complexity: o(logn)
# space complexity: o(1)
