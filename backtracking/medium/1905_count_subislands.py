def countSubIslands(grid1, grid2):
    ROWS, COLS = len(grid2), len(grid2[0])
    vis = set()
    res = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS:
            return True
        
        if (r, c) in vis or grid2[r][c] != 1:
            return True
        
        vis.add((r, c))

        res = True if grid1[r][c] == 1 else False

        res = dfs(r + 1, c) and res
        res = dfs(r - 1, c) and res
        res = dfs(r, c + 1) and res
        res = dfs(r, c - 1) and res

        return res

    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) not in vis and grid2[i][j] == 1 and dfs(i, j):
                res += 1

    return res

print(countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))

# time complexity: o(m * n)
# time complexity: o(m * n)