class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)

        dp_cache = [False] * (n+1)
        dp_cache[n] = True

        for i in range(n-1, -1, -1):
            for each in wordDict:
                if each[0] == s[i] and i + len(each) <= n:
                    if s[i:i+len(each)] == each and not dp_cache[i]:
                        dp_cache[i] = dp_cache[i+len(each)]

        # print(dp_cache)
        return dp_cache[0]