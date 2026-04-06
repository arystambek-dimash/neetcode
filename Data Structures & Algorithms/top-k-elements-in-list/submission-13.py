class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        print(sorted_d)
        return [sorted_d[i][0] for i in range(k)]