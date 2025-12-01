class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        if len(connections) < n-1:
            return -1

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(e1,e2):
            n1 = find(e1)
            n2 = find(e2)
            if n1 == n2:
                return 
            if rank[n1] > rank[n2]:
                parent[n2] = n1
                rank[n1] += 1
            else:
                parent[n1] = n2
                rank[n2] += 1
            return 0
        
        for a,b in connections:
            union(a,b)
        
        components = set()
        for i in range(n):
            components.add(find(i))
        
        return len(components) - 1