class Solution:
    def sumOfDistancesInTree(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        count = [1] * n  # count[i] = number of nodes in subtree i
        distance = [0] * n  # distance[i] = sum of distances in subtree i
        answer = [0] * n
        
        def dfs1(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs1(child, node)
                    count[node] += count[child]
                    distance[node] += distance[child] + count[child]
        
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    answer[child] = answer[node] - count[child] + (n - count[child])
                    dfs2(child, node)
        
        dfs1(0, -1)
        answer[0] = distance[0]
        dfs2(0, -1)
        
        return answer