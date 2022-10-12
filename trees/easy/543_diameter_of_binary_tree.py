import collections


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter(root):
    res = 0

    def dfs(root):
        nonlocal res
        if not root:
            return 0
        l = dfs(root.left)
        r = dfs(root.right)
        res = max(res, l + r)
        return 1 + max(l, r)

    dfs(root)
    return res


def printList(root):
    q = collections.deque()
    q.append(root)
    while q:
        curr = q.popleft()
        print(curr.val)
        q.append(curr.left if curr.left else None)
        q.append(curr.right if curr.right else None)


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)

print(diameter(root))

# time complexity: o(n)
# space complexity: o(n)
