class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # ハッシュマップを利用
        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in "({[":
                stack.append(char)
                
            elif char in bracket_map:
                if not stack:  # stack == []
                    return False
                popchar = stack.pop()
                if popchar != bracket_map[char]:
                    return False
            else:
                return False
        return not stack