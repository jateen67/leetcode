def maxArea(height):
    l = 0
    r = len(height) - 1
    area = 0
    while l < r:
        h = min(height[l], height[r])
        width = r - l
        if h * width > area:
            area = h * width
        if height[l] < height[r]:
            l += 1
        elif height[l] >= height[r]:
            r -= 1
    return area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# time complexity: o(n)
# space complexity: o(1)
