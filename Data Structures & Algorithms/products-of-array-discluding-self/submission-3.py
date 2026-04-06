class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nulls = 0
        _idx = 0
        total = 1
        for idx, i in enumerate(nums):
            if i == 0:
                nulls += 1
                _idx = idx
            if nulls == 2:
                return [0] * len(nums)
            if i != 0:
                total*=i
        arr = []
        if nulls == 0:
            print("nulls 0")
            print(total)
            for i in range(len(nums)):
                print(nums[i])
                arr.append(total // nums[i])
        else:
            arr = [0] * len(nums)
            print(_idx)
            arr[_idx] = total
        return arr