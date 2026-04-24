class MinStack:
    from collections import deque

    def __init__(self):
        self.s = collections.deque()

    def push(self, val: int) -> None:
        self.s.append(val)

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return min(self.s)