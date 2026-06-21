class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_map = defaultdict(int)

        for i, v in enumerate(nums):
            if (target - v) in freq_map:
                return [freq_map[target - v], i]
            freq_map[v] = i