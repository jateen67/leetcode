class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA, headB):
    curr_a = headA
    curr_b = headB
    curr_a_length = 0
    curr_b_length = 0

    while curr_a:
        curr_a = curr_a.next
        curr_a_length += 1

    while curr_b:
        curr_b = curr_b.next
        curr_b_length += 1

    diff = curr_b_length - curr_a_length

    curr_a = headA
    curr_b = headB

    while diff > 0:
        curr_b = curr_b.next
        diff -= 1

    while diff < 0:
        curr_a = curr_a.next
        diff += 1

    while True:
        if curr_a == curr_b:
            return curr_a.val
        curr_a = curr_a.next
        curr_b = curr_b.next


m = ListNode(4)
m.next = ListNode(1)
m.next.next = ListNode(8)
m.next.next.next = ListNode(4)
m.next.next.next.next = ListNode(5)

n = ListNode(5)
n.next = ListNode(6)
n.next.next = ListNode(1)
n.next.next.next = m.next.next


print(getIntersectionNode(m, n))

# time complexity: o(m + n)
# space complexity: o(1)
