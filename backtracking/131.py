class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def dfs(i):
            if i >= len(s):
                result.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        def isPalindrome(i,j):
            # print(i,j)
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        dfs(0)
        return result