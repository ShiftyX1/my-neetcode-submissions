class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        left = 0
        right = l - 1
        for i in range(l):
            if not s[left].isalnum():
                left += 1
                continue
            
            if not s[right].isalnum():
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True 