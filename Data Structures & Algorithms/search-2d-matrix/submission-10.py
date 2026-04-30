class Solution:
    def searchMatrix(self, matrixes: List[List[int]], target: int) -> bool:
        arr = []
        for m in matrixes:
            arr.extend(m)
        
        l = 0
        r = len(arr)
        while l < r:
            m = (r + l) // 2
            if arr[m] == target:
                return True
            elif arr[m] > target:
                r-=1
            else:
                l+=1
        return False