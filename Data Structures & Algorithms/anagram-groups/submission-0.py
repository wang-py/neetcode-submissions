class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            fingerprint = [0] * 26 #freq of 26 lowercase letters
            for one_char in s:
                fingerprint[ord(one_char) - 97] += 1
            
            anagrams[tuple(fingerprint)].append(s)
        
        return list(anagrams.values())