# https://leetcode.com/problems/valid-palindrome/
# o(n) time and space

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleaning the string of spaces
        strippedstr = ""
        for i in s:
            if i.isalnum():
                strippedstr += i
        strippedstr = strippedstr.lower()

        left = 0
        right = len(strippedstr) - 1

        while left <= right:
            if strippedstr[left] != strippedstr[right]:
                return False
            left += 1
            right -= 1
        return True