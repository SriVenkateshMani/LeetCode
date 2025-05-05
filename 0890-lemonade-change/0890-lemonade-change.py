class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in bills:
            if i == 10:
                if five == 0:
                    return False
                ten += 1
                five -= 1
            elif i == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif ten == 0 and five > 2:
                    five -= 3
                else:
                    return False
            else:
                five += 1
        return True

