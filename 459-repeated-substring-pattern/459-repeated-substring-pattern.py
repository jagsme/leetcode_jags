class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(0, len(s)//2):
            if s[0:i + 1] * (len(s) // (i + 1)) == s:
                return True
        return False