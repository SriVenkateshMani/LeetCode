class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(l,r, arr):
            while l <= r:
                mid = (l+r) // 2
                if arr[mid] > target:
                    r = mid - 1
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    return True
            
            return False
        
        left, right = 0, len(matrix)-1
        row = -1

        while left <= right:
            mp = (left + right) // 2

            if matrix[mp][0] <= target <= matrix[mp][-1]:
                row = mp
                break
            
            elif target < matrix[mp][0]:
                right = mp - 1
            
            else:
                left = mp + 1
        
        if row == -1:
            return False
        
        return binary_search(0, len(matrix[row])-1, matrix[row])