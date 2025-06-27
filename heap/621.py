class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        freq = [0] * 26

        for i in tasks:
            freq[ord(i)-ord('A')] += 1
        
        max_heap = []
        for i in range (len(freq)):
            if freq[i] != 0:
                heapq.heappush(max_heap, (-freq[i], chr(i + ord('A'))))
        
        q = deque()

        while len(max_heap) != 0 or len(q) != 0:
            time += 1
            
            if max_heap:
                freq, task = heapq.heappop(max_heap)
                if freq+1 < 0:
                    q.append((task, freq+1, time+n))
            
            if q and q[0][2] == time:
                task, freq, x = q.popleft()
                heapq.heappush(max_heap, (freq, task))
        
        return time
                