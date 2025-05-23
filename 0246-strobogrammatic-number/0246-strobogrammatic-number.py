class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        map = {"0" : "0", "1" : "1", "6" : "9", "8" : "8", "9" : "6"}

        if len(num) == 1:
            return num in ["0", "1", "8"]

        else:
            left = 0
            right = len(num) - 1

            while left <= right:
                if num[left] in map and map[num[left]] == num[right]:
                    left += 1
                    right -= 1
                else:
                    return False
                
            return True