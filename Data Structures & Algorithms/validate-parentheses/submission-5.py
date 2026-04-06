class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:
                    return False
                p = stack.pop() + i
                if p in ']})':
                    return False
                if p not in '[]{}()':
                    return False
        if stack:
            return False
        return True
