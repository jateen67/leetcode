def lengthOfLastWord(s):
    res = 0
    r = len(s) - 1

    while s[r] == " ":
        r -= 1

    while s[r] != " ":
        if r < 0:
            break
        r -= 1
        res += 1

    return res


print(lengthOfLastWord("this is a test   "))


# time complexity: o(n)
# space complexity: o(1)
