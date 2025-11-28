class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # how many of each element do we have left?
        left = {}
        # how many subsequences end in element i
        subs = {}
        for i in nums:
            left[i] = 1 + left.get(i, 0)
            subs[i] = 0
        
        for i in nums:
            if left[i] == 0:
                continue
            left[i] -= 1
            # if we have a subsequence to place i in
            if i-1 in subs and subs[i-1] > 0:
                subs[i] += 1
                subs[i-1] -= 1
            # if we have enough elements to create a new subsequence
            elif i+1 in left and i+2 in left and left[i+1] > 0 and left[i+2] > 0:
                left[i+1] -= 1
                left[i+2] -= 1
                # we're creating a new subsequence that now ends in i + 2
                subs[i+2] += 1
            # if we can't do either of the things above, we can't place this element
            else:
                return False
            

        return True