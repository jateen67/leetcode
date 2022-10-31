import math


def speed(piles, h):
    l, r = 1, max(piles)
    res = r
    while l <= r:
        mid = (l + r) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)

        if hours <= h:
            res = min(res, mid)
            r = mid - 1
        else:
            l = mid + 1
    return res


print(speed([3, 6, 7, 11], 8))

# time complexity: o(nlog(max(n)))
# space complexity: o(1)
