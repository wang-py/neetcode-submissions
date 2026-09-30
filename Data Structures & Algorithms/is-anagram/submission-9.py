class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and all(s.count(c) == t.count(c) for c in set(s))