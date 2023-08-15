def reverseString(s):
    l, r = 0, len(s) - 1

    while l < r:
        tmp = s[l]
        s[l] = s[r]
        s[r] = tmp
        l += 1
        r -= 1

    return s


print(reverseString(["h", "e", "l", "l", "o"]))

# time complexity: o(n)
# space complexity: o(1)
