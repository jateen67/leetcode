def solution(N):
    d = 0
    string = str(N)

    for i in range(len(string)):
        if string[i] == '5':
            if string[0] != '-':
                d = i
                if i + 1 < len(string) and string[i] < string[i + 1]:
                    break
            else:
                d = len(string) - i
                if i + 1 > len(string) and string[i] > string[i + 1]:
                    break

    return string[:d] + string[d + 1:]


def solution2(N):
    string = str(N)
    res = -999_999

    for i in range(len(string)):
        if string[i] == '5':
            new_number = string[:i] + '' + string[i + 1:]
            res = max(res, int(new_number))

    return res


print(solution('-5222675'))
print(solution2('-5222675'))
