class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        curr = []
        result = []

        def backtrack(i):
            if len(curr) == 4 and i == len(s):
                result.append(".".join(curr))
                return
            if len(curr) > 4:
                return

            for j in range(i,len(s)):
                num = int(s[i:j+1])
                # check for leading zeroes
                if num == 0 and len(s[i:j+1]) == 1:
                    curr.append(s[i:j+1])
                    backtrack(j+1)
                    curr.pop()
                # check for valid number
                elif 0 <= num <= 255 and s[i] != '0':
                    curr.append(s[i:j+1])
                    backtrack(j+1)
                    curr.pop()
                elif num > 255:
                    break
        backtrack(0)
        return result
