class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            l = list(s)
            l.sort()
            sorted_l = "".join(l)
            if sorted_l in d:
                d[sorted_l].append(s)
            else:
                d[sorted_l] = [s]
        return list(d.values())