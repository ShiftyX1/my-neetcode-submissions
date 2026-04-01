class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers_set = set(nums)
        result = 0
        for i in numbers_set:
            if i - 1 not in numbers_set:
                length = 0
                while i + length in numbers_set:
                    length += 1
                result = max(length, result)
        return result
            