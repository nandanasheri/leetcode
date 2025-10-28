class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_map = defaultdict(list)
        # building out adjacency map
        for i,j in edges:
            adj_map[i].append(j)
            adj_map[j].append(i)
        
        edge_count = defaultdict(int)
        leaves = deque()

        if edges == []:
            return [0]

        for x in adj_map:
            if len(adj_map[x]) == 1:
                leaves.append(x)
            edge_count[x] += len(adj_map[x])
        
        # Layer order traversal
        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                curr = leaves.popleft()
                n -= 1
                for nei in adj_map[curr]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        leaves.append(nei)

            
            