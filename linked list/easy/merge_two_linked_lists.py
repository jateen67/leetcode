class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    dummy = Node()
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    printList(dummy.next)


def printList(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


n = Node(1)
n.next = Node(2)
n.next.next = Node(4)
n2 = Node(1)
n2.next = Node(3)
n2.next.next = Node(4)
mergeTwoLists(n, n2)

# time complexity: o(n)
# space complexity: o(n)
