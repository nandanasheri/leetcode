class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_map = {}
        s_map = {}
        for i in p:
            p_map[i] = 1 + p_map.get(i,0)


        # do we have more chars in our window than what we need?
        def is_mismatch():
            for i in p_map:
                if s_map.get(i,0) > p_map[i]:
                    return True
            return False

        l = 0
        res = []
        for r in range(len(s)):
            # if char is not in p, it can never be an anagram
            if s[r] not in p_map:
                # clear your window
                l = r + 1
                s_map.clear()
                continue
            # update frequency
            s_map[s[r]] = 1 + s_map.get(s[r], 0)
            # print(l,r, s_map)
            # if we find a match
            if s_map == p_map:
                res.append(l)
                s_map[s[l]] -= 1
                # shift window by 1
                l += 1
            while is_mismatch():
                s_map[s[l]] -= 1
                l += 1
        return res
            