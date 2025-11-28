class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # prices array which will have the minimum cost to reach that node
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            temp = prices.copy()
            for s,d,p in flights:
                # this is an unreachable source node 
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < temp[d]:
                    temp[d] = prices[s] + p
            prices = temp
        
        if prices[dst] == float("inf"):
            return -1
        return prices[dst]

            