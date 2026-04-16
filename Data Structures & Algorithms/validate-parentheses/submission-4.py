class Solution:
    def isValid(self, s: str) -> bool:
        # closing = {')', ']', '}'}
        # opening = {'(', '[', '{'}
        pairs: dict = {')': '(', ']': '[', '}': '{'}
        l = []
        for c in s:
            if c in pairs.keys() and len(l) == 0:
                return False
            
            if c in pairs.values():
                l.append(c)
                continue
            
            if c in pairs.keys() and l[-1] == pairs[c]:
                l.pop()
                continue
            else:
                return False

        return True if len(l) == 0 else False