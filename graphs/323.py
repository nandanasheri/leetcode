class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # parent array and rank array
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            curr = node
            while curr != parent[curr]:
                # path compression
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            return curr
        
        def union(e1,e2):
            n1 = find(e1)
            n2 = find(e2)
            # they are already merged, we do nothing
            if n1 == n2:x
                return 0
            if rank[n1] > rank[n2]:
                parent[n2] = n1
                rank[n1] += 1
            else:
                parent[n1] = n2
                rank[n2] += 1
            # if we merge them together - we return 1!
            return 1
        unions = 0
        for e1,e2 in edges:
            unions += union(e1,e2)
        return n-unions


