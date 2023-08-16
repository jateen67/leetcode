import collections


class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)

    def pop(self):
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self):
        return self.q[-1]

    def empty(self):
        return len(self.q) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
obj.top()
obj.pop()
obj.empty()

# pushing, peeking, is empty: o(1)
# popping: o(n)
