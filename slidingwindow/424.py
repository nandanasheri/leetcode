# https://leetcode.com/problems/longest-repeating-character-replacement/
# barely counts as getting it overcomplicated it - not sure what was my fault still
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        start, end = 0, 0
        max_length = 0
        freq_map = defaultdict(int)

        def max_frequency():
            max_freq = 0
            for i in freq_map:
                max_freq = max(max_freq, freq_map[i])
            return max_freq

        for end in range(len(s)):
            
            freq_map[s[end]] += 1
            replacements = (end - start + 1) - max_frequency()
            
            while replacements > k:
                freq_map[s[start]] -= 1
                start += 1
                replacements = end - start + 1 - max_frequency()
              
            max_length = max(max_length, end - start +1)
                
            

        return max_length
        