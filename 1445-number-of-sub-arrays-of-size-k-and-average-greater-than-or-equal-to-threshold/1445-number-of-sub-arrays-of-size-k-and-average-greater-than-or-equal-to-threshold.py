class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        i, j = 0,0
        curr_sum = 0
        n = len(arr)

        while j < n:
            curr_sum += arr[j]
            
            if (j-i+1 == k):
                avg = curr_sum // k
                if avg >= threshold:
                    res += 1

                curr_sum -= arr[i]
                i += 1
            j += 1
        
        return res
            