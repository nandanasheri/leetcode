class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj_map = defaultdict(list)

        for i in edges:
            adj_map[i[0]].append(i[1])
            adj_map[i[1]].append(i[0])
        
        def dfs(i, camefrom):
            if i in visited:
                return
            visited.add(i)
            for each in adj_map[i]:
                if each == camefrom:
                    continue
                dfs(each, i)
        
        result = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                result += 1

        return result