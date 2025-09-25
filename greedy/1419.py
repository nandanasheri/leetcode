class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # to hold frequencies 
        freq = [0] * 5
        c,r,o,a,k = 0,1,2,3,4
        if len(croakOfFrogs) % 5 != 0:
            return -1
        # calculate frequencies and check for invalid combinations
        # number of frogs in USE
        frogs = 0
        # result
        result = 0

        for i in croakOfFrogs:
            if i == 'c':
                freq[c] += 1
                frogs += 1
            if i == 'r':
                if freq[c] > freq[r]:
                    freq[r] += 1
                else:
                    return -1
            if i == 'o':
                if freq[r] > freq[o]:
                    freq[o] += 1
                else:
                    return -1
            if i == 'a':
                if freq[o] > freq[a]:
                    freq[a] += 1
                else:
                    return -1
            if i == 'k': 
                if freq[a] > freq[k]:
                    freq[k] += 1
                    frogs -=1
                else: 
                    return -1
            result = max(frogs, result)
        
        for i in range(4):
            if freq[i] != freq[i+1]:
                return -1
        
        return result
                