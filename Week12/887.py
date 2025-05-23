class Solution:
    def superEggDrop(self, k, n):
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        moves = 0
        while dp[moves][k] < n:
            moves += 1
            for eggs in range(1, k + 1):
                dp[moves][eggs] = dp[moves - 1][eggs - 1] + dp[moves - 1][eggs] + 1
        
        return moves