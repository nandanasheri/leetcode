class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = defaultdict(int)
        res = []
        for i in s:
            freq[i] += 1
        
        currsize = 0
        currset = set()
        for i in s:
            freq[i] -= 1
            currset.add(i)
            currsize += 1

            match = 0
            for token in currset:
                if freq[token] == 0:
                    match += 1
            
            if match == len(currset):
                res.append(currsize)
                currsize = 0
                currset.clear()
                
        return res
