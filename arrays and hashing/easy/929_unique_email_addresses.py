def numUniqueEmails(emails):
    s = set()

    for i in range(len(emails)):
        j = 0
        email = ""

        while emails[i][j] != "@" and emails[i][j] != "+":
            if emails[i][j] != ".":
                email += emails[i][j]
            j += 1

        while emails[i][j] != "@":
            j += 1

        while j < len(emails[i]):
            email += emails[i][j]
            j += 1

        s.add(email)

    return len(s)


print(numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))

# time complexity: o(N) -> N = number of characters in all words combined
# space complexity: o(n)
