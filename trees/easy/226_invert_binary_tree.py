class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertBinaryTree(root):
    if not root:
        return None
    tmp = root.left
    root.left = root.right
    root.right = tmp
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)
    return root


def printLevel(root, level):
    if root is None:
        return False

    if level == 1:
        print(root.val, end=' ')
        return True

    left = printLevel(root.left, level - 1)
    right = printLevel(root.right, level - 1)

    return left or right


def levelOrderTraversal(root):
    level = 1
    while printLevel(root, level):
        level = level + 1
    print('\n')


n = Node(4)
n.left = Node(2)
n.right = Node(7)
n.left.left = Node(1)
n.left.right = Node(3)
n.right.left = Node(6)
n.right.right = Node(9)
levelOrderTraversal(n)
print('\n')
invertBinaryTree(n)
levelOrderTraversal(n)

# time complexity: o(n)
# space complexity: o(h) h being the height of the tree since because of recursion more method calls will be placed on the application memory stack
