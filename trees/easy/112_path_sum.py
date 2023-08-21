class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    if not root:
        return False

    if not (root.left or root.right):
        return root.val == targetSum

    targetSum -= root.val

    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)


n = TreeNode(5)
n.left = TreeNode(4)
n.left.left = TreeNode(11)
n.left.left.left = TreeNode(7)
n.left.left.right = TreeNode(2)
n.right = TreeNode(8)
n.right.left = TreeNode(13)
n.right.right = TreeNode(4)
n.right.right.right = TreeNode(1)

print(hasPathSum(n, 22))

# time complexity: o(n)
# space complexity: o(n)
