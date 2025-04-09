class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, [], result)
        return result
    
    def backtrack(self, nums, path, result):
        if not nums:
            result.append(path[:])
            return
        
        for i in range(len(nums)):

            current = nums[i]

            remaining_nums = nums[:i] + nums[i+1:]

            path.append(current)

            self.backtrack(remaining_nums, path, result)

            path.pop()