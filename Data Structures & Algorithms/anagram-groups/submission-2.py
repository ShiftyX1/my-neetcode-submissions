class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            hashmap[tuple(count)].append(s)
        return list(hashmap.values())



        # if len(s) != len(t):
        #     return False
        # counter = dict()
        # for char in s:
        #     counter[char] = counter.get(char, 0) + 1

        # for char in t:
        #     counter[char] = counter.get(char, 0) - 1
        # return all(v == 0 for v in counter.values())