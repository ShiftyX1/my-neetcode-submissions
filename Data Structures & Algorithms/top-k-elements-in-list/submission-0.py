class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        if k == 1:
            sorted(counter.keys())
        return sorted(counter.keys())[k - 1:]