class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n)
        freq = defaultdict(int)

        for i in nums:
            if i in freq:
                return True
            freq[i] += 1
        
        return False
