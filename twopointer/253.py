class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        n = len(intervals)
        for i,j in intervals:
            start.append(i)
            end.append(j)
        start.sort()
        end.sort()
        start_ptr, end_ptr = 0,0
        curr = 0
        result = 0

        while start_ptr < n or end_ptr < n:
            if start_ptr < n and end_ptr < n:
                if start[start_ptr] < end[end_ptr]:
                    curr += 1
                    start_ptr += 1
                # if we end before we start or if tie, we end first 
                else:
                    curr -= 1
                    end_ptr += 1
            elif start_ptr < n:
                curr += 1
                start_ptr += 1
            else:
                curr -= 1
                end_ptr += 1
            result = max(result, curr)
        return result
            
