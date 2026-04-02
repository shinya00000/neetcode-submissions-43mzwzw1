class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set() 
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        for i in range(9):
            seen = set() 
            for j in range(9):
                val = board[j][i]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        for i in range(3):
            for j in range(3):
                seen = set()
                for k in range(3):
                    for l in range(3):
                        val = board[i*3+k][j*3+l]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)
        return True