class Solution:
    from collections import deque
    def evalRPN(self, tokens: List[str]) -> int:
        stack_num = deque([])
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack_num.append(int(tokens[i]))
            else:
                num_right = stack_num.pop()
                num_left = stack_num.pop()
                if tokens[i] == "+":
                    num_res = num_left + num_right
                    stack_num.append(num_res)
                elif tokens[i] == "-":
                    num_res = num_left - num_right
                    stack_num.append(num_res)
                elif tokens[i] == "*":
                    num_res = num_left * num_right
                    stack_num.append(num_res)
                elif tokens[i] == "/":
                    """
                    if num_left < 0 and num_right > 0:
                        num_res = - (abs(num_left) // abs(num_right))
                    elif num_left > 0 and num_right < 0:
                        num_res = - (abs(num_left) // abs(num_right))
                    else:
                        num_res = num_left // num_right
                    #print(num_left, num_right, num_res)
                    """
                    num_res = int(num_left / num_right)
                    stack_num.append(num_res)
                else:
                    print("Error")
                    return 100000000
        return stack_num.pop()

