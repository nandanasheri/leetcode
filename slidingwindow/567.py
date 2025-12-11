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

            
