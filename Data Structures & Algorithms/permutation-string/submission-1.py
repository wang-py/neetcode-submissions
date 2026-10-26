class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1 = [0] * 26

        # sliding window
        l, r = 0, len(s1)
        # check character frequency
        for c in s1:
            freq1[ord(c) - 97] += 1
        
        while r <= len(s2):
            freq2 = [0] * 26
            for c in s2[l:r]:
                freq2[ord(c) - 97] += 1
            if freq1 == freq2:
                return True
            else:
                l += 1
                r += 1
        
        return False