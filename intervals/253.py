"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        max_count = 0
        start, end = [], []

        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        
        # sort both start and end times
        start.sort()
        end.sort()

        i, j = 0, 0

        while i < len(start):
            # if two meetings overlap then increment count
            if start[i] < end[j]:
                count += 1
                i += 1
            # a meeting has ended so decrement count
            else:
                j += 1
                count -=1
            max_count = max(max_count, count)
        return max_count




        