class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if s in t:
            return t
        freq_t = {}
        for i in t:
            freq_t[i] = freq_t.get(i, 0) + 1
        window = []
        indexes = {}
        found = 0
        res = ""
        tt = set(list(t))
        for i in range(len(s)):
            freq_i = {}
            if s[i] in t:
                indexes[s[i]] = i
                if len(indexes) == len(tt):
                    values = indexes.values()
                    f = min(values)
                    second = max(values)
                    w = s[f: second + 1]
                    for j in w:
                        freq_i[j] = freq_i.get(j, 0) + 1
                    is_valid = True
                    for k,v in freq_i.items():
                        if k in freq_t and freq_t.get(k) > v:
                            is_valid = False
                            break
                    if is_valid:
                        if not res:
                            res = w
                        elif len(w) < len(res):
                            res = w
        return res