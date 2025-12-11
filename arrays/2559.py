class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * len(words)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        csum = 0
        result = []
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                csum += 1
            prefix[i] = csum
        
        for start, end in queries:
            if start == 0:
                result.append(prefix[end])
            else:
                result.append(prefix[end]-prefix[start-1])
        # print(prefix)
        return result


        