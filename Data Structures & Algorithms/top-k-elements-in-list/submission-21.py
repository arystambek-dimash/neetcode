class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for key,freq in d.items():
            bucket[freq].append(key)
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for b in bucket[i]:
                res.append(b)
                if len(res) == k:
                    return res