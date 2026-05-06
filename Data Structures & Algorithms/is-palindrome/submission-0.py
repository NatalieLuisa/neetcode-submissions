class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the string
        s = ''.join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(s) - 1

        # Compare characters using two pointers
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True



