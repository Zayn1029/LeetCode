class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        target_mask = (1 << n) - 1
        queue = [(i, 1 << i) for i in range(n)]
        visited = set(queue)
        steps = 0
        
        while queue:
            next_queue = []
            for node, mask in queue:
                if mask == target_mask:
                    return steps
                
                for neighbor in graph[node]:
                    next_mask = mask | (1 << neighbor)
                    next_state = (neighbor, next_mask)
                    
                    if next_state not in visited:
                        visited.add(next_state)
                        next_queue.append(next_state)
            
            queue = next_queue
            steps += 1
        
        return steps