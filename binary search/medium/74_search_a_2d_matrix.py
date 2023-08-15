def search(matrix, target):
    l_rows = 0
    r_rows = len(matrix) - 1
    mid_rows = 0

    while l_rows <= r_rows:
        mid_rows = (l_rows + r_rows) // 2

        if target < matrix[mid_rows][0]:
            r_rows = mid_rows - 1
        elif target > matrix[mid_rows][-1]:
            l_rows = mid_rows + 1
        else:
            break

    l = 0
    r = len(matrix[0]) - 1

    while l <= r:
        mid = (l + r) // 2

        if target == matrix[mid_rows][mid]:
            return True
        elif target > matrix[mid_rows][mid]:
            l = mid + 1
        else:
            r = mid - 1
    return False


print(search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

# time complexity: o(log(m*n))
# space complxity: o(1)
