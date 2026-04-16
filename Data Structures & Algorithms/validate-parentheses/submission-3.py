class Solution:
    def isValid(self, s: str) -> bool:
        closing = {')', ']', '}'}
        opening = {'(', '[', '{'}
        pairs = {')': '(', ']': '[', '}': '{'}
        l = []
        for c in s:
            if c in closing and len(l) == 0:
                return False
            
            if c in opening:
                l.append(c)
                continue
            
            if c in closing and l[-1] == pairs[c]:
                l.pop()
                continue
            else:
                return False

        return True if len(l) == 0 else False