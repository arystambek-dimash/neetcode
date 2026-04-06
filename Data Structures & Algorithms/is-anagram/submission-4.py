class Solution:
    def isAnagram(self, sstr1: str, sstr2: str) -> bool:
        d = {}
        if len(sstr1) > len(sstr2):
            return False
        for s in sstr1:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        
        for s in sstr2:
            if s not in d:
                return False
            d[s]-=1
            if d[s] < 0:
                return False
        return True