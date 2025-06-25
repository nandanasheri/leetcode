class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        curr = []

        num_map = {}
        start = ord('a')
        limit = 3
        for i in range(2, 10):
            num_map[i] = []
            if i == 7 or i == 9:
                limit = 4
            else:
                limit = 3
            for j in range(limit):
                num_map[i].append(chr(start))
                start += 1
        
        def dfs(i):
            # print(i, curr)
            if len(curr) == len(digits):
                result.append(''.join(curr))
                return
            for j in num_map[int(digits[i])]:
                curr.append(j)
                dfs(i+1)
                curr.pop()
        
        if len(digits):
            dfs(0)
        return result