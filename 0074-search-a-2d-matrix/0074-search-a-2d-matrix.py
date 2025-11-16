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
        
        for arr in matrix:
            if binary_search(0, len(arr)-1, arr):
                return True
        return False