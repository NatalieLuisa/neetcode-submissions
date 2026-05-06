class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s[::-1]) == sorted(t[::-1])