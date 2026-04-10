class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        while l < r:
            while l < len(s) and not any([s[l].isalpha(), s[l].isdigit()]):
                l+=1
            while r > 0 and not any([s[r].isalpha(), s[r].isdigit()]):
                r-=1
            if l < r and s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True