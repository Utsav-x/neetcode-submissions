class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            width = r - l
            area = max(area,width * min(heights[l],heights[r]))    
            
            if  heights[l] < heights[r]:
                l += 1
                width += 1
            else:
                r -= 1
                width += 1
        return area