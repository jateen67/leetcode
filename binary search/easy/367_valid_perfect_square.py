def isPerfectSquare(num):
    l, r = 1, num

    while l <= r:
        mid = (l + r) // 2

        if mid**2 == num:
            return True
        elif mid**2 < num:
            l = mid + 1
        else:
            r = mid - 1

    return False


print(isPerfectSquare(16))

# time complexity: o(logn)
# space complexity: o(1)
