class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in '+-*/':
                b = stack.pop()
                a = stack.pop()
                stack.append(self.calculate(a, b, t))
            else:
                stack.append(int(t))
        return stack[0]

    def calculate(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            return int(a / b)
