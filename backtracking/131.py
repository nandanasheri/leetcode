class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def dfs(i):
            if i == len(s):
                res.append(curr[::])
                return
            for j in range(i, len(s)):
                curr_s = s[i:j+1]
                # if valid palindrome partition
                if curr_s == curr_s[::-1]:
                    curr.append(curr_s)
                    dfs(j+1)
                    curr.pop()
        dfs(0)
        return res