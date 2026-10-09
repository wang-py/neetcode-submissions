class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower_case = [x.lower() for x in s if x.isalnum()]
        length = len(s_lower_case)
        for i in range(length):
            if s_lower_case[i] != s_lower_case[length - 1 - i]:
                return False
        
        return True