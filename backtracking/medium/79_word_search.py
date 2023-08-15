def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    vis = set()

    def dfs(r, c, i):
        if i == len(word):
            return True

        if r < 0 or c < 0 or r == ROWS or c == COLS:
            return False

        if (r, c) in vis or board[r][c] != word[i]:
            return False

        vis.add((r, c))

        res = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )

        vis.remove((r, c))

        return res

    for i in range(ROWS):
        for j in range(COLS):
            if dfs(i, j, 0):
                return True

    return False


print(
    exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
)

# time complexity: o(m*n*4^len(word))
# space complexity: o(m*n)
