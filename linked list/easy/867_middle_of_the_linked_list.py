class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val


n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n.next.next.next = ListNode(4)
n.next.next.next.next = ListNode(5)
n.next.next.next.next.next = ListNode(6)

print(middleNode(n))

# time complexity: o(n)
# space complexity: o(1)
