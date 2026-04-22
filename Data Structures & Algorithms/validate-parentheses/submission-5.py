class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char == ")":
                if stack == []:
                    return False
                popchar = stack.pop()
                if popchar != "(":
                    return False
            elif char == "}":
                if stack == []:
                    return False
                popchar = stack.pop()
                if popchar != "{":
                    return False
            elif char == "]":
                if stack == []:
                    return False
                popchar = stack.pop()
                if popchar != "[":
                    return False
            else:
                return False
        if stack != []:
            return False
        return True