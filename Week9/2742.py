class Solution:
    def paintWalls(self, cost, time):
        n = len(cost)
        dp = {}
        
        def dfs(i, remaining):
            if remaining <= 0:
                return 0
            if i == n:
                return float('inf')
            if (i, remaining) in dp:
                return dp[(i, remaining)]
            
            paint = cost[i] + dfs(i + 1, remaining - 1 - time[i])
            skip = dfs(i + 1, remaining)
            
            dp[(i, remaining)] = min(paint, skip)
            return dp[(i, remaining)]
        
        return dfs(0, n)