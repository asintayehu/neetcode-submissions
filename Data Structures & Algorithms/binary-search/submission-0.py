class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Initialize relevant pointers

        l_ptr= 0
        r_ptr= len(nums)-1

        while l_ptr <= r_ptr:

            # set mid to floor(avrg)
            mid= (l_ptr + r_ptr)// 2

            if nums[mid] < target:
                l_ptr= mid + 1
            
            elif nums[mid] > target:
                r_ptr = mid - 1
            
            else:
                return mid
            
        return -1