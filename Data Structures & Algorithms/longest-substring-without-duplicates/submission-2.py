class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        count = 0
        m = 0
        for i in s:
            while i in window:
                window.pop(0)
                count-=1
            else:
                count+=1
            window.append(i)
            m = max(m, count)
        return m