class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minheap = []
        result = []

        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda t : t[0])

        i = 0
        time = tasks[0][0]

        while minheap or i < len(tasks):
            # while there is still tasks to be processed and current time is past the enqueue time
            while i < len(tasks) and time >= tasks[i][0]:
                e, p, ind = tasks[i]
                heapq.heappush(minheap, (p, ind))
                i += 1
            # if our minheap is non empty
            if minheap:
                process, ind = heapq.heappop(minheap)
                result.append(ind)
                time += process
            # CPU is sitting idle - we need to pass time (fast forward)
            else:
                time = tasks[i][0]


        return result