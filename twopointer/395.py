class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def longest_substr(start, end):
            if end - start < k:
                return 0

            char_map = {}
            for i in range(start, end):
                char_map[s[i]] = char_map.get(s[i], 0) + 1
            

            for i in range(start, end):
                if char_map[s[i]] >= k:
                    continue
                # if you hit an invalid character
                invalid = i+1
                while invalid < end and char_map[s[invalid]] < k:
                    invalid += 1
                return max(longest_substr(start, i), longest_substr(invalid, end))
            # no invalid chars, whole thing is valid
            return end - start
        
        return longest_substr(0, len(s))
