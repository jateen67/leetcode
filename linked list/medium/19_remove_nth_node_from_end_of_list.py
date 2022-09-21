class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove(head, n):
    dummy = Node(next=head)
    left, right = dummy, dummy

    while n >= 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next

    return dummy.next


def printList(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


n = Node(1)
n.next = Node(2)
n.next.next = Node(3)
n.next.next.next = Node(4)
n.next.next.next.next = Node(5)

printList(remove(n, 2))

# time complexity: o(n)
# space complexity: o(1)
