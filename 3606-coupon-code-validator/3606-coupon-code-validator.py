class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = []
        n = len(code)
        p_map = {"electronics": 1 , "grocery": 2, "pharmacy": 3, "restaurant": 4}
        buckets = {1:[], 2:[], 3:[], 4:[]}

        for i in range(n):
            if isActive[i] and businessLine[i] in p_map :
                
                if not code[i]:
                    continue

                valid = True
                for ch in code[i]:
                    if not(ch.isalnum() or ch == '_'):
                        valid = False
                        break
                
                if valid:
                    priority = p_map[businessLine[i]]
                    buckets[priority].append(code[i])
        
        for p in [1,2,3,4]:
            buckets[p].sort()
            res.extend(buckets[p])
        
        return res