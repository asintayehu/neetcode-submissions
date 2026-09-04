class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_size= len(matrix[0])-1

        for idx in range(0, len(matrix)):
                l_ptr= matrix[idx][0]
                r_ptr= matrix[idx][row_size]
                
                if target <= r_ptr and target >= l_ptr:
                    return self.binary_search(matrix[idx], target)
                    
        return False
    

    def binary_search(self, array, target):

        l_ptr= 0
        r_ptr= len(array)-1

        while l_ptr <= r_ptr:

            mid= (l_ptr + r_ptr) // 2

            if array[mid] < target:
                l_ptr= mid + 1
            
            elif array[mid] > target:
                r_ptr= mid - 1
           
            else:
                return True

        return False