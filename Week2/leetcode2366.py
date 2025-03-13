class Solution:
    def minimumReplacement(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
            
        operations = 0

        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
            
            parts = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
            
            operations += parts - 1
            
            nums[i] = nums[i] // parts
        
        return operations