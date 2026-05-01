class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_square = 0
        for p in range(len(heights)):
            min_height = float('inf')
            width = 0
            for i in range(p, len(heights)):
                if heights[i] < min_height:
                    square = min_height * width
                    if square > max_square:
                        max_square = square
                    min_height = heights[i]
                width += 1
            square = min_height * width
            if square > max_square:
                        max_square = square
        return max_square