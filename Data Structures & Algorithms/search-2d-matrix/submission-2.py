class Solution:
    def search_column(self, n_l: int, n_r: int, array: List[int], target: int) -> bool:
        if n_l > n_r:
            return False
        n_i = n_l + (n_r - n_l) // 2
        if array[n_i] == target:
            return True
        elif array[n_i] > target:
            return self.search_column(n_l, n_i - 1, array, target)
        else: # array[n_i] < target
            return self.search_column(n_i + 1, n_r, array, target)



    def search_row(self, m_l: int, m_r: int, matrix: List[List[int]], target: int) -> bool:
        if m_l > m_r:
            return False
        m_i = m_l + (m_r - m_l) // 2
        if matrix[m_i][0] > target:
            return self.search_row(m_l, m_i - 1, matrix, target)
        elif matrix[m_i][-1] < target:
            return self.search_row(m_i + 1, m_r, matrix, target)
        else: # matrix[m_i][0] <= target <= matrix[m_i + 1][0]
            return self.search_column(0, len(matrix[m_i]), matrix[m_i], target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.search_row(0, len(matrix) - 1, matrix, target)

            
                