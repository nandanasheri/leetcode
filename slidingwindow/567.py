class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1            

        l = 0
        
        for r in range(len(s1), len(s2)):
            if freq1 == freq2:
                return True
            
            index = ord(s2[r]) - ord('a')
            freq2[index] += 1

            index = ord(s2[l]) - ord('a')
            freq2[index] -= 1

            l += 1
        
        return freq1 == freq2

        # also you can do this using a matches variable so it goes from o(26n) to o(n+26)


        