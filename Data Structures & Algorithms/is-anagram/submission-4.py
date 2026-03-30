class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = dict()
        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for char in t:
            counter[char] = counter.get(char, 0) - 1
        return all(v == 0 for v in counter.values())