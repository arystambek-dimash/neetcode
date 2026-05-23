class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        print(nums)
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[left] + nums[right] + nums[i]
                if s == 0:
                    if [nums[left], nums[right], nums[i]] not in arr:
                        arr.append([nums[left], nums[right], nums[i]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s > 0:
                    right-=1
                elif s < 0:
                    left+=1 
        return arr
