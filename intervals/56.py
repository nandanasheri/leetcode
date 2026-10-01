class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        sorted_intervals = sorted(intervals)
        result = []
        result.append(sorted_intervals[0])

        for i in range(1, len(sorted_intervals)):
            start, end = sorted_intervals[i][0], sorted_intervals[i][1]
            prev_start, prev_end = result[-1][0], result[-1][1]
            if prev_end >= start:
                result[-1] = [min(prev_start, start), max(prev_end, end)] 
            else:
                result.append([start, end])
        return result