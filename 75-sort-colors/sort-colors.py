class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums) - 1
        cur = 0

        while cur <= end:
            if nums[cur] == 0:
                nums[cur], nums[start] = nums[start], nums[cur]
                cur += 1
                start += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[end] = nums[end], nums[cur]
                end -= 1