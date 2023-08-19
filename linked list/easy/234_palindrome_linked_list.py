class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None

    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    left, right = head, prev

    while right:
        if left.val != right.val:
            return False

        left = left.next
        right = right.next

    return True


n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(2)
n.next.next.next = ListNode(1)

print(isPalindrome(n))

# time complexity: o(n)
# space complexity: o(1)
