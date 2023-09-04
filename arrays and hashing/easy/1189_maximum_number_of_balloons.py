def maxNumberOfBalloons(text):
    balloon = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
    hm = {}
    res = float("inf")

    for c in text:
        hm[c] = hm.get(c, 0) + 1

    for c in balloon:
        res = min(res, hm.get(c, 0) // balloon[c])

    return res


print(maxNumberOfBalloons("loonbalxballpoon"))

# time complexity: o(n)
# time complexity: o(n)
