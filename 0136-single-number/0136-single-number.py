class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_map = defaultdict(int)
        for i in nums:
            count_map[i] += 1

        for key, value in count_map.items():
            if value == 1:
                return key