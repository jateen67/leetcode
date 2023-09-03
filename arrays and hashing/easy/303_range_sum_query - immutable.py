class NumArray:
    def __init__(self, nums):
        self.prefix = []
        s = 0
        for num in nums:
            s += num
            self.prefix.append(s)

    def sumRange(self, left, right):
        return (
            self.prefix[right]
            if left == 0
            else self.prefix[right] - self.prefix[left - 1]
        )
