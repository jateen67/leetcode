def sub(s):
    l = 0
    res = 0
    hs = set()

    for r in range(len(s)):
        while s[r] in hs:
            hs.remove(s[l])
            l += 1
        hs.add(s[r])
        res = max(res, r - l + 1)

    return res


print(sub('abcabcbb'))

# time complexity: o(n)
# space complexity: o(n)
