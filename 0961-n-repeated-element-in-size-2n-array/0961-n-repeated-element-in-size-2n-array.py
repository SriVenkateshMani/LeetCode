class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
        
        for key, value in freq.items():
            if value > 1:
                return key