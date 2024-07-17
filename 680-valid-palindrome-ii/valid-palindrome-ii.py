class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                st1 = s[:l] + s[l+1:]
                st2 = s[:r] + s[r+1:]
                return st1 == st1[::-1] or st2 == st2[::-1]
            l += 1
            r -= 1
        return True