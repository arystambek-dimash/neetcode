class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1,2,4,6]

        [1,1,2,8]
        [48,24,6,1]

        prefix = [1]
        for i in range(len(nums) - 1):
            prefix.append(nums[i] * prefix[i])
        
        curr = 1
        for i in range(len(nums) - 1 , -1 ,-1):
            temp = nums[i]
            nums[i] = curr

            curr *= temp
        res = []
        for p,s in zip(prefix, nums):
            res.append(p * s)
        return res
