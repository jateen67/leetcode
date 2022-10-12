class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        self.minStack.append(min(val, self.minStack[-1]))

    def pop(self):
        if self.stack:
            self.stack.pop()
        if self.minStack:
            self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

# time complexity: o(1)
# space complxity: o(n)
