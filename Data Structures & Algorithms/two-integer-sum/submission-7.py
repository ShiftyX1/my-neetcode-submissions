class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # counter = {num: for i, num in enumerate(nums)}
        for i in nums:
            complement = target - i
            
                
