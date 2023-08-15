import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    if not root:
        return root

    q = collections.deque()
    q.appendleft(root)
    res = []

    while q:
        level = []

        for i in range(len(q)):
            popped = q.popleft()

            level.append(popped.val)

            if popped.left:
                q.append(popped.left)

            if popped.right:
                q.append(popped.right)

        res.append(level)

    return res


n = TreeNode(3)
n.left = TreeNode(9)
n.right = TreeNode(20)
n.right.left = TreeNode(15)
n.right.right = TreeNode(7)

print(levelOrder(n))

# time complexity: o(n)
# space complexity: o(2^h)
