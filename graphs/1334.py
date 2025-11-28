class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjmap = defaultdict(list)

        for u,v,d in edges:
            adjmap[u].append((v,d))
            adjmap[v].append((u,d))

        def dijkstra(start):
            pq = []
            heapq.heappush(pq, (0, start))
            visited = set()
            result = 0
            while pq:
                dist, curr = heapq.heappop(pq)
                if curr in visited or dist > distanceThreshold:
                    continue
                visited.add(curr)
                if curr != start:
                    result += 1
                for nei, d in adjmap[curr]:
                    if nei not in visited and dist + d <= distanceThreshold:
                        heapq.heappush(pq,(dist+d, nei))
            return result
            

        min_cities = n
        res = 0
        for i in range(n):
            count = dijkstra(i)
            if count <= min_cities:
                min_cities = count
                res = i
        return res