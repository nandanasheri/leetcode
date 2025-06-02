# https://leetcode.com/problems/group-anagrams/description/
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string, make sorted string key and value is list of unsorted strings
        freq_map = {}
        '''for i in strs:
            sorted_i = tuple(sorted(i))
            freq_map[sorted_i] = freq_map.get(sorted_i, []) + [i]'''

        for i in strs:
            freq = [0] * 26
            for j in i:
                freq[97 - ord(j)] += 1
            freq_map[tuple(freq)] = freq_map.get(tuple(freq), []) + [i]
        
        return list(freq_map.values())