def characterReplacement(s, k):
    hm = {}
    res = 0
    l = 0

    for r in range(len(s)):
        hm[s[r]] = hm.get(s[r], 0) + 1

        while r - l + 1 - max(hm.values()) > k:
            hm[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res


print(characterReplacement("AABABBA", 1))

# time complexity: o(n)
# time complexity: o(n)
