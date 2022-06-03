class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_ans = 0
        for i in range(len(num)):
            num_ans = num_ans*10 + num[i]
        return [int(d) for d in str(num_ans+k)]
        