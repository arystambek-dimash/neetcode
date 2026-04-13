class Solution:
    def is_alpha(self, char):
        return (
            (char >= 'A' and char <= 'Z') 
            or 
            (char >= 'a' and char <= 'z')
            or
            (char >= '0' and char <= '9')
        )
    
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        while l <= r:
            while l < r and not self.is_alpha(s[l]):
                l+=1
            while l < r and not self.is_alpha(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True