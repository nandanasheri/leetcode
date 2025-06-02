# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency map and sort array - nlogn solution
        countmap = {}
        for i in nums:
            countmap[i] = countmap.get(i,0) + 1
        
        '''arr = []
        for i in countmap:
            arr.append([countmap[i], i])
        list.sort(arr)
        
        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res'''
        
        # max heap solution still nlogn solution
        '''max_heap = []
        for i in countmap:
            heapq.heappush(max_heap, (-countmap[i], i))
        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res'''

        bucket_arr = [[] for i in range(len(nums) + 1)]
        for i in countmap:
            bucket_arr[countmap[i]].append(i)
     
        res = []
        for i in range(len(bucket_arr)-1, 0, -1):
            for j in bucket_arr[i]:
                res.append(j)
                if len(res) == k:
                    return res



        

