class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head):
    prev = None
    curr = head

    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    printList(prev)


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
reverseLinkedList(n)

# time complexity: o(n)
# space complexity: o(1)
