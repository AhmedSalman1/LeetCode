class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h_set = set(nums)
        res = 0

        for num in h_set:
            if (num - 1) not in h_set:
                length = 1
                while (num + length) in h_set:
                    length += 1
                res = max(length, res)
        return res