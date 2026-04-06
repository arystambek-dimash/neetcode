class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)
        
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        for num, cnt in d.items():
            freq[cnt].append(num)
        print(freq)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    print(res)
                    return res