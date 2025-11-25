class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build out adjacency map
        adj_map = defaultdict(list)
        nodes = 0
        for u,v,w in times:
            adj_map[u].append((v,w))

        visited = set()
        time = 0
        minheap = []
        heapq.heappush(minheap, (0,k))
        # BFS w Dijkstra
        while minheap:
            path, curr = heapq.heappop(minheap)
            if curr in visited:
                continue
            visited.add(curr)
            time = max(time,path)
            for nei in adj_map[curr]:
                if nei[0] not in visited:
                    heapq.heappush(minheap, (path+nei[1], nei[0]))
        
        if len(visited) != n:
            return -1

        return time
