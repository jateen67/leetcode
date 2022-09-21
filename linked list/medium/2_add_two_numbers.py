class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = Node()
    tail = dummy
    carry = 0

    while l1 or l2 or carry:
        l1v = l1.val if l1 else None
        l2v = l2.val if l2 else None

        added = l1v + l2v + carry
        carry = added // 10
        added = added % 10
        new_node = Node(added)

        tail.next = new_node

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        tail = tail.next

    printList(dummy.next)


def printList(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


n = Node(2)
n.next = Node(4)
n.next.next = Node(3)
n2 = Node(5)
n2.next = Node(6)
n2.next.next = Node(4)
addTwoNumbers(n, n2)

# time complexity: o(n)
# space complexity: o(n)
