class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = defaultdict(int)
        
        for i in hand:
            freq[i] += 1
        minheap = list(freq.keys())
        heapq.heapify(minheap)
        
        while minheap:
            first = minheap[0]
            for i in range(first, first+groupSize):
                print(i)
                if i not in freq:
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True
                

    
        
        