class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []
        for current_tok in tokens:
            # print(f"current token is {current_tok}")
            # print(f"num1: {num1}, num2: {num2}")
            if current_tok == "+":
                number_stack.append(number_stack.pop() + number_stack.pop())
            elif current_tok == "-":
                num2 = number_stack.pop()
                num1 = number_stack.pop()
                number_stack.append(num1 - num2)
            elif current_tok == "*":
                number_stack.append(number_stack.pop() * number_stack.pop())
            elif current_tok == "/":
                num2 = number_stack.pop()
                num1 = number_stack.pop()
                number_stack.append(int(num1 / num2))
            else:
                number_stack.append(int(current_tok))
            # print(f"number stack is {number_stack}")
        
        return number_stack[-1]
        

