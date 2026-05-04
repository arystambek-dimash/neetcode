class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2 
            works = 0
            for pile in piles:
                works += math.ceil(pile / m)
            print(works)
            if works <= h:
                r = m
            else:
                l = m + 1

        return l