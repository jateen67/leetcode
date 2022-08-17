class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = Node()
    tail = dummy
    carry = 0

    while l1 or l2 or carry:
        l1v = 0
        l2v = 0
        if l1:
            l1v = l1.val
        if l2:
            l2v = l2.val
        added = l1v + l2v + carry
        carry = added // 10
        new_node = Node(added)
        if added >= 10:
            new_node.val -= 10
        tail.next = new_node
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
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
