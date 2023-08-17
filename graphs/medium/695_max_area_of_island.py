def maxAreaOfIsland(grid):
    ROWS, COLS = len(grid), len(grid[0])
    vis = set()
    res = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS:
            return 0

        if (r, c) in vis or grid[r][c] != 1:
            return 0

        vis.add((r, c))

        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    for i in range(ROWS):
        for j in range(COLS):
            res = max(dfs(i, j), res)

    return res


print(
    maxAreaOfIsland(
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
)

# time complexity: o(m * n)
# space complexity: o(m * n)
