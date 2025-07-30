class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        result = []

        for i in range(len(intervals)):
            sub = intervals[i]
            # ends before the new interval starts
            if sub[1] < start:
                result.append(sub)
            # starts after the new interval ends
            elif sub[0] > end:
                result.append([start, end])
                return result + intervals[i:]
            else:
                start = min(start, sub[0])
                end = max(end, sub[1])

        result.append([start, end])
      
        return result