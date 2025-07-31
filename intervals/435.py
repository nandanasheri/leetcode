class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals = sorted(intervals)
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            # check for overlap
            if end > intervals[i][0]:
                result += 1
                end = min(end, intervals[i][1])
            else:
                end = intervals[i][1]
        
        return result

