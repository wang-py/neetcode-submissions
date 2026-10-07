class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}':'{', ']':'['}
        open_brackets = ['(', '{', '[']
        open_stack = []
        length = len(s)
        if length == 1:
            return False
        for i in range(length):
            if s[i] in open_brackets:
                open_stack.append(s[i])
            elif open_stack:
                if brackets[s[i]] != open_stack.pop():
                    print(f"brackets is {brackets[s[i]]}")
                    return False 
            else:
                return False
        
        if open_stack:
            return False
        
        return True