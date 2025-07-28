class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        i, j = 0,0
        #avg = 0
        curr_sum = 0
        n = len(arr)

        while j < n:
            if (j-i+1 < k):
                curr_sum += arr[j]
                j += 1
            
            elif (j-i+1 == k):
                curr_sum += arr[j]
                avg = curr_sum // k
                if avg >= threshold:
                    res += 1

                curr_sum -= arr[i]
                i += 1
                j += 1
        
        return res
            