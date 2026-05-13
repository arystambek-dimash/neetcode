class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        m = 0
        temp = []
        for i in range(k):
            temp.append(nums[i])
        res.append(max(temp))

        for i in range(len(nums) - k):
            temp.pop(0)
            temp.append(nums[i+k])
            res.append(max(temp))
        
        return res