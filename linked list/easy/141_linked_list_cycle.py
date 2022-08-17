class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def cycle(head):
    # h = set()
    # curr = head
    # while curr:
    #     if curr in h:
    #         return True
    #     h.add(curr)
    #     curr = curr.next
    # return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


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
print(cycle(n))

# time complexitt: o(n)
# space complexity: o(n) with hashmap, o(1) with 2 pointers
