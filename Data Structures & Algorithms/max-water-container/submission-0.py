class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        s_max = 0
        while i < j:
            s = (j - i) * min(heights[i], heights[j])
            s_max = max(s, s_max)
            if heights[i] < heights[j]:
                i += 1
            else :
                j -= 1
        return s_max