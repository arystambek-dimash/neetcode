class Solution:
    def sort(self, s):
        arr = [0] * 26
        for ch in s:
            arr[ord(ch) - ord('a')] += 1
        res = ""
        for i, a in enumerate(arr):
            idx = a
            while idx != 0:
                res+=chr(i + ord('a'))
                idx-=1
        return res
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for s in strs:
            ss = self.sort(s)
            dd[ss].append(s)
        return list(dd.values())