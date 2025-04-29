from collections import deque

class Solution:
    def openLock(self, deadends, target):

        deadends = set(deadends)

        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        
        # BFS
        queue = deque([("0000", 0)])  
        visited = set(["0000"])  
        
        while queue:
            curr_comb, turns = queue.popleft()

            for i in range(4):
                for direction in [-1, 1]:

                    digit = (int(curr_comb[i]) + direction) % 10

                    next_comb = curr_comb[:i] + str(digit) + curr_comb[i+1:]

                    if next_comb == target:
                        return turns + 1

                    if next_comb not in deadends and next_comb not in visited:
                        visited.add(next_comb)
                        queue.append((next_comb, turns + 1))

        return -1