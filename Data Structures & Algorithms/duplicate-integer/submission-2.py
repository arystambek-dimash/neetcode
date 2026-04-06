class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = None
        for n in nums:
            if prev is not None and prev == n:
                return True
            prev = n
        return False