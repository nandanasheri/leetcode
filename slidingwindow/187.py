class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        freqMap = {}
        result = []

        l = 0
        if len(s) < 10:
            return []
        for r in range(9, len(s)):
            freqMap[s[l:r+1]] = freqMap.get(s[l:r+1], 0) + 1
            l += 1
        for k in freqMap:
            if freqMap[k] > 1:
                result.append(k)
        return result