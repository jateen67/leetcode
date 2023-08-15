def mergeAlternately(word1, word2):
    res = ""

    l, r = 0, 0

    while l < len(word1) and r < len(word2):
        res += word1[l]
        res += word2[r]
        l += 1
        r += 1

    if l < len(word1):
        while l < len(word1):
            res += word1[l]
            l += 1

    if r < len(word2):
        while r < len(word2):
            res += word2[r]
            r += 1

    return res


print(mergeAlternately("abc", "pqr"))

# time complexity: o(s + t)
# space complexity: o(1)
