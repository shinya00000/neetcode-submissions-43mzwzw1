class Solution:
    from collections import deque
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if temperatures == []:
            return []
        stack = deque([])
        res = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and stack[-1][1] < temp:
                res[stack[-1][0]] = (i - stack[-1][0])
                stack.pop()
            stack.append([i, temp])

        return res