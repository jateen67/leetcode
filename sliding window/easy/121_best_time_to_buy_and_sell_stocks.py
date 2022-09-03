def maxProfit(prices):
    l = 0
    r = 1
    max_profit = 0

    while r < len(prices):
        profit = prices[r] - prices[l]
        if profit < 0:
            l += 1
            continue
        if profit > max_profit:
            max_profit = profit
        r += 1
    return max_profit


print(maxProfit([1, 2, 3, 4, 5, 6]))

# time complexity: o(n)
# space complexity: o(1)
