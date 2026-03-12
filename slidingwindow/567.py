class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = {}
        map2 = {}
        for i in range(len(s2)):
            map1[s2[i]] = 0
            map2[s2[i]] = 0
            
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            map1[s1[i]] = map1.get(s1[i], 0) + 1
            map2[s2[i]] += 1

        l, r = 0, len(s1) - 1

        while r < len(s2):
            # print(map1, map2, l, r)
            if map1 == map2:
                return True
            r += 1
            if r == len(s2):
                break
            map2[s2[r]] += 1
            map2[s2[l]] -= 1
            l += 1
        return False
    
    # another solution using matches - more complicated o(n) purely

    class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        char_map1 = [0] * 26
        char_map2 = [0] * 26
        matches = 0

        for i in range(len(s1)):
            char_map1[ord(s1[i])-ord('a')] += 1
            char_map2[ord(s2[i])-ord('a')] += 1
        
        # o(26) operation
        for i in range(26):
            if char_map1[i] == char_map2[i]:
                matches += 1
        l = 0
        r = len(s1)
        while r < len(s2):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            char_map2[index] += 1
            if char_map1[index] == char_map2[index]:
                matches += 1
            elif char_map1[index] + 1 == char_map2[index]:
                matches -= 1
            # print(matches, s2[r])

            index = ord(s2[l]) - ord('a')
            char_map2[index] -= 1
            if char_map1[index] == char_map2[index]:
                matches += 1
            elif char_map1[index] - 1 == char_map2[index]:
                matches -= 1
            l += 1
            r += 1
        
        if matches == 26:
            return True
        return False


            
