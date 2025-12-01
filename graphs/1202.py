class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            curr = node
            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            return curr
        
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
            return 
        # create connected components using union find
        for i,j in pairs:
            union(i,j)

        # build the connected components into a dict of lists where root -> component
        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)
            
        # sort chars within each connected component
        sorted_chars = {}
        for c in components:
            chars = []
            for i in components[c]:
                chars.append(s[i])
            # i sort in reverse to pop from the back conveniently
            chars.sort(reverse=True)
            sorted_chars[c] = chars

        # iterate through indices and build out the result
        result = ""
        for i in range(n):
            result += sorted_chars[find(i)].pop()
        return result

        