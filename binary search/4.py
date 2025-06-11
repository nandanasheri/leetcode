# this broke me o(log(m+n)) solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2
        if len(A) > len(B):
            A,B = B,A
        l = 0
        r = len(A) - 1
        
        while True:
            mid = (l+r) // 2
            mid2 = half - mid - 2 # intuitively you take the partition of the left  index position
            # check whether our partitions are correct
            Aleft = A[mid] if mid >= 0 else float("-infinity")
            Aright = A[mid+1] if mid+1 < len(A) else float("infinity")
            Bleft = B[mid2] if mid2 >= 0 else float("-infinity")
            Bright = B[mid2+1] if mid2 + 1 < len(B) else float("infinity")
            
            
            if Aleft <= Bright and Bleft <= Aright:
                break
            elif Bleft > Aright:
                l = mid + 1
            else:
                r = mid - 1
        
        if total % 2 == 1:
            return min(Aright, Bright)
        else:
            left = max(Aleft, Bleft)
            right = min(Aright, Bright)
            return (left+right)  / 2
            
