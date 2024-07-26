class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h_map = {}

        for i, n in enumerate(nums):
            if n in h_map and i - h_map[n] <= k:
                return True
            else:
                h_map[n] = i
        
        return False


        # for i in range(len(nums)):
        #     if nums[i] in h_map and abs(i - h_map[nums[i]]) <= k:
        #         return True

        #     h_map[nums[i]] = i

        # return False