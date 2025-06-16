class Solution:
    def maxDiff(self, num: int) -> int:
        max_num, min_num = str(num), str(num)
        
        # max num
        for i in max_num:
            if i != "9":
                max_num = max_num.replace(i, "9")
                break
        for i, j in enumerate(min_num):
            if i == 0:
                if j != "1":
                    min_num = min_num.replace(j, "1")
                    break
            else:
                if j != "0" and j != "1":
                    min_num = min_num.replace(j, "0")
                    break
        
        return int(max_num)- int(min_num)

