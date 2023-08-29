def islandPerimeter(grid):
    ROWS, COLS = len(grid), len(grid[0])
    vis = set()
    res = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] != 1:
            return 1

        if (r, c) in vis:
            return 0

        vis.add((r, c))

        return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                res += dfs(i, j)

    return res

    # ROWS, COLS = len(grid), len(grid[0])
    # res = 0

    # for i in range(ROWS):
    #     for j in range(COLS):
    #         if grid[i][j] == 1:
    #             res += 4
    #             if i > 0 and grid[i - 1][j] == 1:
    #                 res -= 1
    #             if j > 0 and grid[i][j - 1] == 1:
    #                 res -= 1
    #             if i < ROWS - 1 and grid[i + 1][j] == 1:
    #                 res -= 1
    #             if j < COLS - 1 and grid[i][j + 1] == 1:
    #                 res -= 1

    # return res


print(islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))

# time complexity: o(m * n)
# space complexity: o(m * n)

# optimized time complexity: o(m * n)
# optimized space complexity: o(1)
