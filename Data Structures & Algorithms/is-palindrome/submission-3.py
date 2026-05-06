class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri = ''
        for c in s:
            if c.isalnum():
                stri += c.lower()
        return stri == stri[::-1]