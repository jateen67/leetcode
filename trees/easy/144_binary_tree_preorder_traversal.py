class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root):
    curr = root
    stack, res = [], []

    while curr or stack:
        if curr:
            res.append(curr.val)
            stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()

    return res


n = Node(1)
n.right = Node(2)
n.right.left = Node(3)

print(preorderTraversal(n))

# time complexity: o(n)
# space complexity: o(n)
