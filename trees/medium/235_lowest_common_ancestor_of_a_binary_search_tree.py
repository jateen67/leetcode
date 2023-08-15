class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    while root:
        if (p.val < root.val) and (q.val < root.val):
            root = root.left
        elif (p.val > root.val) and (q.val > root.val):
            root = root.right
        else:
            return root.val


n = TreeNode(6)
n.left = TreeNode(2)
n.left.left = TreeNode(0)
n.left.right = TreeNode(4)
n.left.right.left = TreeNode(3)
n.left.right.right = TreeNode(5)
n.right = TreeNode(8)
n.right.left = TreeNode(7)
n.right.right = TreeNode(9)

print(lowestCommonAncestor(n, TreeNode(2), TreeNode(8)))

# time complexity: o(h)
# space complexity: o(1)
