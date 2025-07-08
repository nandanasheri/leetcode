class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        path = set()
        visited = set()
        adj_map = defaultdict(list)

        for i in edges:
            adj_map[i[0]].append(i[1])
            adj_map[i[1]].append(i[0])
        
        def dfs(i, parent):
            if i in path:
                return False
            path.add(i)
            for each in adj_map[i]:
                if each == parent:
                    continue
                if not dfs(each, i):
                    return False
            path.remove(i)
            visited.add(i)
            return True
        
        dfs(0, -1)
        
        for i in range(n):
            if i not in visited:
                return False
        return True