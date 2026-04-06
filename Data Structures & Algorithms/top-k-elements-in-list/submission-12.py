class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        print(d)
        sorted_d = reversed(sorted(d.items(), key=lambda x:x[1]))
        return [t[0] for t in sorted_d][:k]