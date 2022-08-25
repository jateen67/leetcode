def isPalindrome(s):
    d = ''.join(c for c in s if c.isalnum()).lower()
    p1 = 0
    p2 = len(d) - 1
    while p1 < p2:
        if d[p1] != d[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True


print(isPalindrome('jeej'))

# time complexity: o(n)
# space complexity: o(1)
