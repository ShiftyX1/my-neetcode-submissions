class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}_{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = list()
        i = 0
        while i < len(s):
            j = s.index("_", i)
            length = int(s[i:j])
            res.append(s[j + 1 : j+1 + length])
            i = j + 1 + length
        return res