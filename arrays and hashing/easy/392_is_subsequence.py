def isSubsequence(s, t):
    if not s:
        return True

    l = 0

    for r in range(len(t)):
        if s[l] == t[r]:
            l += 1
        if l == len(s):
            return True

    return False


print(isSubsequence("ace", "abcdef"))
# time complexity: o(s + t)
# space complexity: o(1)
