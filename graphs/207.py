class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        adj_map = defaultdict(list)
        # set up adjacency map
        for i in prerequisites:
            adj_map[i[0]].append(i[1])
        
        def dfs(course):
            # print(course, path)
            if course in path:
                return False
            if adj_map[course] == []:
                return True
            path.add(course)
            for prereq in adj_map[course]:
                if not dfs(prereq):
                    return False
            path.remove(course)
            adj_map[course] = []
            return True
        
        for i in range(numCourses):
            path.clear()
            if not dfs(i):
                return False
        return True