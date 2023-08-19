class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    if not head:
        return

    prev, curr = head, head.next

    while curr:
        if curr.val == prev.val:
            curr = curr.next
            prev.next = curr
        else:
            curr = curr.next
            prev = prev.next

    printList(head)


def printList(head):
    curr = head

    while curr:
        print(curr.val)
        curr = curr.next


n = ListNode(1)
n.next = ListNode(1)
n.next.next = ListNode(2)
n.next.next.next = ListNode(4)
n.next.next.next.next = ListNode(4)

print(deleteDuplicates(n))

# time complexity: o(n)
# space complexity: o(1)
