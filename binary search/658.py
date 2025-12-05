class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # use binary search to find closest element to k
        min_diff = float("inf")
        min_index = -1
        l,r = 0, len(arr) - 1
        while l <= r:
            # print(l,r)
            mid = (l+r) // 2
            if arr[mid] == x:
                min_diff = 0
                min_index = mid
                break
            diff = abs(arr[mid]-x)
            if diff < min_diff:
                min_diff = diff
                min_index = mid
            if diff == min_diff and arr[mid] < arr[min_index]:
                min_diff = diff
                min_index = mid
            if arr[mid] > x:
                r = mid - 1
            else:
                l = mid + 1
        
        result = []
        result.append(arr[min_index])

        l = min_index - 1
        r = min_index + 1
        # use two pointer solution once you use binary search to find the elements closest to index
        while len(result) < k:
            # print(l,r,result)
            if 0<=l<len(arr) and 0<=r<len(arr):
                if abs(arr[l]-x) <= abs(arr[r]-x) :
                    result.append(arr[l])
                    l -= 1
                else:
                    result.append(arr[r])
                    r += 1
            elif 0<=l<len(arr):
                result.append(arr[l])
                l -= 1
            else:
                result.append(arr[r])
                r += 1
        return sorted(result)
