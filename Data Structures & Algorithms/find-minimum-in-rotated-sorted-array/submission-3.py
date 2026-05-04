class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[l] > nums[r]:
                l = l + 1
            else:
                r = r - 1
            print(l, r, m)
        return nums[l]