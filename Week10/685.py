class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        parent = [0] * (n + 1)
        
        candidate1, candidate2 = None, None
        
        for u, v in edges:
            if parent[v] == 0:
                parent[v] = u
            else:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
                break
        
        for i in range(1, n + 1):
            parent[i] = i
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for i, (u, v) in enumerate(edges):
            if [u, v] == candidate2:
                continue
                
            if find(u) == find(v):
                if candidate1 is None:
                    return [u, v]
                else:
                    return candidate1
                    
            union(u, v)
        
        return candidate2