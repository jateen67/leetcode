class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    def check(root, mini, maxi):
        if not root:
            return True

        if root.val <= mini or root.val >= maxi:
            return False

        return check(root.left, mini, root.val) and check(root.right, root.val, maxi)

    return check(root, float("-inf"), float("inf"))


n = TreeNode(5)
n.left = TreeNode(1)
n.right = TreeNode(4)
n.right.left = TreeNode(3)
n.right.right = TreeNode(6)

print(isValidBST(n))

# time complexity: o(n)
# space complexity: o(n)
