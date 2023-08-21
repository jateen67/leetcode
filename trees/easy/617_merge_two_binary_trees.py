import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(root1, root2):
    def dfs(r1, r2):
        if not (r1 or r2):
            return

        v1 = r1.val if r1 else 0
        v2 = r2.val if r2 else 0

        res = TreeNode(v1 + v2)

        res.left = dfs(r1.left if r1 else None, r2.left if r2 else None)
        res.right = dfs(r1.right if r1 else None, r2.right if r2 else None)

        return res

    return dfs(root1, root2)


def printTree(root):
    q = collections.deque()
    q.appendleft(root)
    res = []

    while q:
        for _ in range(len(q)):
            popped = q.popleft()
            res.append(popped.val)

            if popped.left:
                q.append(popped.left)
            if popped.right:
                q.append(popped.right)

    return res


m = TreeNode(1)
m.left = TreeNode(3)
m.left.left = TreeNode(5)
m.right = TreeNode(2)

n = TreeNode(2)
n.left = TreeNode(1)
n.left.right = TreeNode(4)
n.right = TreeNode(3)
n.right.left = TreeNode(7)

print(printTree(mergeTrees(m, n)))

# time complexity: o(s + t)
# space complexity: o(n)
