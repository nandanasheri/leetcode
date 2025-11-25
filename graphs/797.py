class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = []
        visited = set()
        adj_map = {}
        target = len(graph) - 1
        for i in range(len(graph)):
            adj_map[i] = graph[i]
        
        def dfs(i):
            if i == target:
                # print(path)
                res.append(path[::])
                return
            for n in adj_map[i]:
                path.append(n)
                dfs(n)
                path.pop()
        
        path.append(0)
        dfs(0)
        return res