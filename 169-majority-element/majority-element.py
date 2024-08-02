class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
            
            if dic[num] > len(nums) // 2:
                return num