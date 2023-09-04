def wordPattern(pattern, s):
    char_to_word, word_to_char = {}, {}
    p = 0

    for i in range(len(pattern)):
        word = ""
        while p < len(s) and s[p] != " ":
            word += s[p]
            p += 1

        if pattern[i] not in char_to_word:
            if word in word_to_char:
                return False
            char_to_word[pattern[i]] = word
            word_to_char[word] = pattern[i]
        else:
            if char_to_word[pattern[i]] != word:
                return False

        if p >= len(s) and i < len(pattern) - 1:
            return False

        if p >= len(s):
            return True

        p += 1


print(wordPattern("abba", "dog cat cat dog"))

# time complexity: o(m + n)
# time complexity: o(n)
