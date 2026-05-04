class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        if nums[l] <= target <= nums[len(nums) - 1]:
            i = l
            r = len(nums) - 1
        else:
            i = 0
            r = l - 1
    
        while i <= r:
            m = (i + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                i  = m + 1
            else:
                r = m - 1
        return -1
            