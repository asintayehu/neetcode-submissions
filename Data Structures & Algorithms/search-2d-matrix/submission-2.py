class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top, bot= 0, len(matrix)-1

        while top <= bot:
            mid_row= (bot + top) // 2

            if target > matrix[mid_row][-1]:
                top= mid_row + 1
            
            elif target < matrix[mid_row][0]:
                bot= mid_row - 1

            else:
                break

        # checking for proper pointer setting
        if not (top <= bot):
            return False
        
        # row we'll be doing binary search
        row= (top + bot) // 2

        # begin binary search
        l_ptr= 0
        r_ptr= len(matrix[row])-1

        while l_ptr <= r_ptr:
            mid= (l_ptr + r_ptr) // 2

            if target < matrix[row][mid]:
                r_ptr= mid - 1

            elif target > matrix[row][mid]:
                l_ptr = mid + 1
            
            else:
                return True

        return False