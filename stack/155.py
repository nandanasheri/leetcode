# https://leetcode.com/problems/min-stack/
# o(n) space and o(1) time 
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minimum.append(val)
        else:
            if val < self.minimum[-1]:
                self.minimum.append(val)
            else:
                self.minimum.append(self.minimum[-1])

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()