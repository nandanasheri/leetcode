class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        fuel = startFuel
        output = 0
        prev = 0

        for dist, gas in stations + [(target,0)]:
            # all dist is absolute to start but we want it to be relative to previous distance 
            # like - how much further have you travelled from before
            fuel -= (dist - prev)
            # print(dist, heap, fuel)
            while heap and fuel < 0:
                g = -heapq.heappop(heap)
                fuel += g
                # we're refilling and we want to refill at the MAX tank
                output += 1
            # even after refilling, fuel is negative
            if fuel < 0:
                return -1
            heapq.heappush(heap,-gas)
            prev = dist
        return output