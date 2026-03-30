class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        
        return list({key: value for key, value in sorted(counter.items(), key=lambda item: item[1], reverse=True)}.keys())[:k]