def isAlienSorted(words, order):
    hm = {}

    for i in range(len(order)):
        hm[order[i]] = i

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]

        for j in range(len(w1)):
            if j == len(w2):
                return False

            if w1[j] != w2[j]:
                if hm[w1[j]] > hm[w2[j]]:
                    return False
                break

    return True


print(isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))

# time complexity: o(m * n)
# space complexity: o(m * n)

# optimized time complexity: o(m * n)
# optimized space complexity: o(1)
