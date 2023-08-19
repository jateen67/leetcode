class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    if not head:
        return

    dummy = ListNode(next=head)
    prev = dummy
    curr = head

    while curr:
        if curr.val == val:
            curr = curr.next
            prev.next = curr
        else:
            curr = curr.next
            prev = prev.next

    printList(dummy.next)


def printList(head):
    curr = head

    while curr:
        print(curr.val)
        curr = curr.next


n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(6)
n.next.next.next = ListNode(3)
n.next.next.next.next = ListNode(4)
n.next.next.next.next.next = ListNode(5)
n.next.next.next.next.next.next = ListNode(6)

print(removeElements(n, 6))

# time complexity: o(n)
# space complexity: o(1)
