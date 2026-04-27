class Solution:
    def maxArea(self, h: List[int]) -> int:
        m = -1
        l = 0
        r = len(h) - 1
        while l <= r:
            m = max(min(h[l], h[r]) * (r - l), m)

            if h[l] >= h[r]:
                r-=1
            else:
                l+=1
        
        return m