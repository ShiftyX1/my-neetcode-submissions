class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # counter = {num: for i, num in enumerate(nums)}
        checked = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in checked.keys():
                return [checked[complement], i]
            checked[num] = i 
                
