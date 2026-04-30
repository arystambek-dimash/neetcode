class Solution:
    def trap(self, heights: List[int]) -> int:
        # min(height[l], height[r]) - height[i]
        l = 0
        r = len(heights) - 1
        _min = 0
        s = 0
        left_max = 0
        right_max = 0
        s = 0
        while l < r:
            left_max = max(left_max, heights[l])
            right_max = max(right_max, heights[r])

            water_at_l = left_max - heights[l]
            water_at_r = right_max - heights[r]
            s += water_at_l + water_at_r
            
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1                
        return s