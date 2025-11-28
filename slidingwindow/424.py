class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqMap = {}
        res = 0

        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            # you can put this in a function
            max_freq = 0
            for i in freqMap:
                max_freq = max(max_freq, freqMap[i])

            while (r-l+1) - max_freq > k:
                freqMap[s[l]] -= 1
                l += 1
                max_freq = 0
                for i in freqMap:
                    max_freq = max(max_freq, freqMap[i])
            res = max(res, r-l+1)
        return res