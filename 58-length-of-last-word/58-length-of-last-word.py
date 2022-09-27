class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        count = len(l) - 1
        while True:
            if l[count].isalpha():
                return len(l[count])
            else:
                count -= 1