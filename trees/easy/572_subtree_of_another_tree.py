class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sub(root, subRoot):
    if not subRoot:
        return True
    if not root:
        return False
    if same(root, subRoot):
        return True
    return sub(root.left, subRoot) or sub(root.right, subRoot)


def same(root, subRoot):
    if not root and not subRoot:
        return True

    if (root and not subRoot) or (subRoot and not root):
        return False

    if root.val != subRoot.val:
        return False

    return same(root.left, subRoot.left) and same(root.right, subRoot.right)


def inOrder(head):
    if not head:
        return None
    inOrder(head.left)
    print(head.val)
    inOrder(head.right)


root = Node(3)
root.left = Node(4)
root.left.left = Node(1)
root.left.right = Node(2)
root.right = Node(5)

subRoot = Node(4)
subRoot.left = Node(1)
subRoot.right = Node(2)

print(sub(root, subRoot))

# time complexity: o(s*t)
# space complexity: o(n)
