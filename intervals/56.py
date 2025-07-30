class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            
            inter = intervals[i]
            curr = result[-1]
            # starts before previous one ended - there is overlap
            if inter[0] <= curr[1]:
                result[-1][1] = max(curr[1], inter[1])
            else:
                result.append(inter)


        return result