class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_int = set(range(1,len(nums)+1))- set(nums)
        if bool(min_int):
            return min(min_int)
        return max(nums) + 1