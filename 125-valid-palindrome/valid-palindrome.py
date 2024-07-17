class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''

        for st in s:
            if st.isalpha() or st.isdigit():
                new += st.lower()
        return new == new[::-1]