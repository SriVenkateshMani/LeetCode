class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = list(str(x))
        if lst == lst[::-1]:
            return True
        else:
            return False