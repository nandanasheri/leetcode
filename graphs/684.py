class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(node):
            if parent[node] == node:
                return node
            # path compression - set parent to grandparent so closer paths
            parent[node] = parent[parent[node]]
            return find(parent[node])
        
        def union(n1, n2):
            node1 = find(n1)
            node2 = find(n2)
            if node1 == node2:
                return False
            if rank[node1] > rank[node2]:
                parent[node2] = node1
                rank[node2] += 1
            else:
                parent[node1] = node2
                rank[node1] += 1
            return True
        
        for a,b in edges:
            isConnected = union(a,b)
            if not isConnected:
                return [a,b]
            