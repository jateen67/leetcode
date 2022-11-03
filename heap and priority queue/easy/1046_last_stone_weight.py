from heapq import heapify, heappop, heappush


def weight(stones):
    for i in range(len(stones)):
        stones[i] *= -1

    heapify(stones)

    while len(stones) > 1:
        x = heappop(stones)
        y = heappop(stones)
        if y > x:
            heappush(stones, x - y)

    return abs(stones[0]) if stones else 0


print(weight([2, 7, 4, 1, 8, 1]))

# time complexity: o(nlog(n))
# space complexity: o(1)
