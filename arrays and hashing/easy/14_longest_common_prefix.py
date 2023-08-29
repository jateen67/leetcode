def longestCommonPrefix(strs):
    res = ""

    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                return res

        res += strs[0][i]

    return res


print(longestCommonPrefix(["flower", "flow", "flight"]))

# time complexity: o(min(n) * m) -> n = length of all words
# space complexity: o(1)
