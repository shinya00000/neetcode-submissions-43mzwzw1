class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 各行，各列，各3x3ブロックの数字の出現をビット（整数）で記録する配列
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                # '1'-'9'を0-8のシフト量に変換（例: '3' -> 2ビットシフト -> 2進数で 000000100）
                bit_mask = 1 << (int(val) - 1)

                # 3x3ブロックのインデックスを計算 (0〜8)
                box_idx = (r // 3) * 3 + (c // 3)

                # ビット積（&）で重複チェック
                # 既にその数字が出現していれば，結果は0以外の値になる
                if (rows[r] & bit_mask) or (cols[c] & bit_mask) or (boxes[box_idx] & bit_mask):
                    return False

                # ビット和（|）で出現した数字を記録
                rows[r] |= bit_mask
                cols[c] |= bit_mask
                boxes[box_idx] |= bit_mask

        return True