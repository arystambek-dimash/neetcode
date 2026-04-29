class MinStack:
    def __init__(self):
        self.stack = []
        self._max = 0
        self._min = 0
    
    def push(self, val: int) -> None:
        self._max = max(self._max, val)
        self._min = min(self._min, val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self._min = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
