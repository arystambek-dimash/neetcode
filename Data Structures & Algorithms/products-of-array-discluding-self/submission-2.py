class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = [0] * len(nums)
        suffixProd = [0] * len(nums)

        suffixProd[-1] = 1
        prefixProd[0] = 1

        for i in range(1, len(nums)):
            prefixProd[i] = prefixProd[i-1] * nums[i-1]
        for i in range(len(nums) - 1, 0, -1):
            print(i)
            suffixProd[i - 1] = nums[i] * suffixProd[i]
        
        ans = []
        for i in range(len(nums)):
            ans.append(prefixProd[i] * suffixProd[i])
        return ans