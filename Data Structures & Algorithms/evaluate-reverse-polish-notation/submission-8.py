class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []
        for current_tok in tokens:
            # print(f"current token is {current_tok}")
            try:
                current_tok = int(current_tok)
                number_stack.append(current_tok)
            except ValueError:
                num2 = number_stack.pop()
                num1 = number_stack.pop()
                # print(f"num1: {num1}, num2: {num2}")
                if current_tok == "+":
                    number_stack.append(num1 + num2)
                elif current_tok == "-":
                    number_stack.append(num1 - num2)
                elif current_tok == "*":
                    number_stack.append(num1 * num2)
                elif current_tok == "/":
                    number_stack.append(int(num1 / num2))
            # print(f"number stack is {number_stack}")
        
        return number_stack[-1]
        

