class Solution:
    def sort(self, s: str) -> str:
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if (ord(s[i]) - ord('a')) > (ord(s[j]) - ord('a')):
                    temp = s[i]
                    s[i] = s[j]
                    s[j] = temp
        return ''.join(s)

    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        print(self.sort(s))
        print(self.sort(t))
        return s == t