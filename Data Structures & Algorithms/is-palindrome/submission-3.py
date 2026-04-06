class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '')
        l = 0
        r = len(s) - 1
        symbols = '?,.\':'
        while l <= r:
            left_s = s[l].lower()
            right_s = s[r].lower()
            if left_s == right_s:
                l+=1
                r-=1
            elif left_s in symbols:
                l+=1
            elif right_s in symbols:
                r-=1
            else:
                return False

        return True