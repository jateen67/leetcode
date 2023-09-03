def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    hm = {}

    for i in range(len(s)):
        if s[i] not in hm:
            if t[i] in hm.values():
                return False
            hm[s[i]] = t[i]

        if t[i] != hm[s[i]]:
            return False

    return True


print(isIsomorphic("egg", "add"))

# time complexity: o(n)
# time complexity: o(n)
