def rotate(matrix):

    l = 0
    r = len(matrix) - 1

    while l < r:
        top = l
        bottom = r
        for i in range(l, r):
            # save the top left
            topLeft = matrix[top][l + i]
            # move bottom left into top right
            matrix[top][l + i] = matrix[bottom - i][l]
            # move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]
            # move top right into bottom right
            matrix[bottom][r - i] = matrix[top + i][r]
            # move top left into top right
            matrix[top + i][r] = topLeft
        r -= 1
        l += 1
    return matrix


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# time complexity: o(n^2)
# space complexity: o(1)
