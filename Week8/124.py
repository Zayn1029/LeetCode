class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))
            
            self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)
            
            return node.val + max(left_sum, right_sum)
        
        dfs(root)
        return self.max_sum