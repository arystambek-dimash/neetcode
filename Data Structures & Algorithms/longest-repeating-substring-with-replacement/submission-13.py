class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(list)
        for i, ch in enumerate(s):
            d[ch].append(i)

        d = dict(d)
        m = 0
        print(d)
        for key, v in d.items():
            l = 0
            tempM = min(len(s), 1 + k)
            need_replace = 0
            for r in range(1, len(v)):
                n = (v[r] - v[r - 1]) - 1
                
                need_replace += n

                while need_replace > k:
                    left_gap = v[l + 1] - v[l] - 1
                    need_replace -= left_gap
                    l+=1
                current_len = need_replace + r - l + 1
                remaining = k - need_replace
                tempM = max(tempM, min(len(s), current_len + remaining))

            m = max(m, tempM)
        return m