class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        duplicates = set()
        for i in nums:
            if i in seen:
                duplicates.add(i)
            else:
                seen.add(i)
        if list(duplicates):
            return True
        return False