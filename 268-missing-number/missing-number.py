class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ex_sum = n * (n + 1) // 2
        nums_sum = sum(nums)

        return ex_sum - nums_sum