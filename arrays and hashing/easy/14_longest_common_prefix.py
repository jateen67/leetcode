def longestCommonPrefix(strs):
    res = ""

    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                return res

        res += strs[0][i]

    return res


print(longestCommonPrefix(["flower", "flow", "flight"]))

# time complexity: o(N) -> N = number of characters in all words combined
# space complexity: o(1)
