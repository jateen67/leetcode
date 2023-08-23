class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head):
    res = 0
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    left, right = head, prev
    while right:
        res = max(res, left.val + right.val)
        left = left.next
        right = right.next

    return res


n = ListNode(5)
n.next = ListNode(4)
n.next.next = ListNode(2)
n.next.next.next = ListNode(1)

print(pairSum(n))

# time complexity: o(n)
# space complexity: o(1)
