class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, cur_sum = 0, 0
        min_sum = float('inf')

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                min_sum = min(min_sum, right - left + 1)
                cur_sum -= nums[left]
                left += 1

        return 0 if min_sum == float('inf') else min_sum