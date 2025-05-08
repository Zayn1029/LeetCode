class Solution:
    def trap(self, height):
        if not height:
            return 0
            
        n = len(height)
        left, right = 0, n - 1
        left_max = height[left]
        right_max = height[right]
        result = 0
        
        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]
                
        return result