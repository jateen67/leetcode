class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return sameTree(p.left, q.left) and sameTree(p.right, q.right)


def printLevel(root, level):
    if root is None:
        return False

    if level == 1:
        print(root.val, end=" ")
        return True

    left = printLevel(root.left, level - 1)
    right = printLevel(root.right, level - 1)

    return left or right


def levelOrderTraversal(root):
    level = 1
    while printLevel(root, level):
        level = level + 1
    print("\n")


n = Node(4)
n.left = Node(2)
n.right = Node(7)

n2 = Node(4)
n2.left = Node(2)
n2.right = Node(7)

levelOrderTraversal(n)
levelOrderTraversal(n2)
print(sameTree(n, n2))

# time complexity: o(min(s, t))
# space complexity: o(h) h being the height of the tree since because of recursion more method calls will be placed on the application memory stack
