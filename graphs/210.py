class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        adj_map = defaultdict(list)
        path = set()
        visited = set()

        for i in prerequisites:
            adj_map[i[0]].append(i[1])
        
        def dfs(i):
            # detects a cycle since it's already in the current path
            if i in path:
                return False
            # we already have this in our output so don't need to add it again
            # we could just check output but that's an o(n) check since it's a list so we use another set
            if i in visited:
                return True

            path.add(i)
            for pre in adj_map[i]:
                if not dfs(pre):
                    return False
            path.remove(i)
            visited.add(i)
            output.append(i)
            # this basically skips extra work if you've gone through it already
            adj_map[i] = []
            return True
        
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output