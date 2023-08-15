class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    curr = root
    stack, res = [], []

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

    return res


n = Node(1)
n.right = Node(2)
n.right.left = Node(3)

print(inorderTraversal(n))

# time complexity: o(n)
# space complexity: o(n)
