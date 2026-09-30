class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ascii = [ord(x) for x in s]
        t_ascii = [ord(x) for x in t]

        if len(s_ascii) != len(t_ascii):
            return False
    
        s_ascii_val = sorted(s_ascii)
        t_ascii_val = sorted(t_ascii)


        return s_ascii_val == t_ascii_val