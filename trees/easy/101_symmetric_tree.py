class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    if not root:
        return True

    def dfs(left, right):
        if not (left or right):
            return True

        if not (left and right):
            return False

        if left.val != right.val:
            return False

        return dfs(left.left, right.right) and dfs(left.right, right.left)

    return dfs(root.left, root.right)


n = TreeNode(1)
n.left = TreeNode(2)
n.left.left = TreeNode(3)
n.left.right = TreeNode(4)
n.right = TreeNode(2)
n.right.left = TreeNode(4)
n.right.right = TreeNode(3)

print(isSymmetric(n))

# time complexity: o(n)
# space complexity: o(n)
