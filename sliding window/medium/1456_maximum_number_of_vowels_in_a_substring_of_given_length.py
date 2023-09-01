def maxVowels(s, k):
    num_vowels, res, l = 0, 0, 0
    vowels = ["a", "e", "i", "o", "u"]

    for r in range(len(s)):
        if s[r] in vowels:
            num_vowels += 1

        if r - l + 1 > k:
            if s[l] in vowels:
                num_vowels -= 1
            l += 1

        res = max(res, num_vowels)

    return res


print(maxVowels("abciiidef", 3))

# time complexity: o(n)
# time complexity: o(1)
