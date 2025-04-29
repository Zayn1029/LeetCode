from collections import deque

class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0

        queue = deque([(0, 0)])
        visited = set([0]) 
        
        # BFS
        while queue:
            curr_amount, coins_used = queue.popleft()

            for coin in coins:
                next_amount = curr_amount + coin

                if next_amount == amount:
                    return coins_used + 1

                if next_amount < amount and next_amount not in visited:
                    visited.add(next_amount)
                    queue.append((next_amount, coins_used + 1))

        return -1