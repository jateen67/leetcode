def validAnagram(s, t):
    elements_in_s = {}
    elements_in_t = {}

    for i in range(len(s)):
        if s[i] not in elements_in_s:
            elements_in_s[s[i]] = 1
        else:
            elements_in_s[s[i]] += 1

    for i in range(len(t)):
        if t[i] not in elements_in_t:
            elements_in_t[t[i]] = 1
        else:
            elements_in_t[t[i]] += 1
    return elements_in_s == elements_in_t


print(validAnagram('car', 'ar'))

# time complexity: o(n)
# space complexity: o(n)
