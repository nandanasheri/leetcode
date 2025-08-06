class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False] * 3
        for i in range(0, len(triplets)):
            # if any of those values are greater then we would not even check because that would be our ceiling
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            # if we have the target values in any of the other arrays then we can combine them but we don't even need to combine
            if triplets[i][0] == target[0]:
                res[0] = True
            if triplets[i][1] == target[1]:
                res[1] = True
            if triplets[i][2] == target[2]:
                res[2] = True
        
        return res == [True, True, True]