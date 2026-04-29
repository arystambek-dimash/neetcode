class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        s = list(s)
        print(s)
        stack = []
        while s:
            l = s.pop()
            if l in ']})':
                stack.append(l)
            else:
                if stack:
                    a = stack.pop()
                    if l+a not in '[]{}()':
                        return False
                else:
                    return False
        if stack:
            return False
        return True