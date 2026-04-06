class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        unq = []

        for n in nums:
            if n not in unq:
                unq.append(n)
        print(unq)
        m = 0
        c = 0
        for i in range(1, len(unq)):
            if unq[i] - unq[i-1] == 1:
                c+=1
            else:
                c = 0
            m = max(m, c)
        
        return m + 1