def numIslands(grid):
    ROWS, COLS = len(grid), len(grid[0])
    vis = set()

    def dfs(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS:
            return 0

        if (r, c) in vis or grid[r][c] != "1":
            return 0

        vis.add((r, c))

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

        return 1

    res = 0

    for i in range(ROWS):
        for j in range(COLS):
            if dfs(i, j) == 1:
                res += 1

    return res


print(
    numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)

# time complexity: o(4*m*n)
# space complexity: o(m*n)
