class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        bin1 = int(a)
        bin2 = int(b)
        if bin1 == 0 and bin2 == 0:
            return '0'
        carry = 0
        while bin1 > 0 or bin2 > 0:
            binary1 = bin1 % 10
            binary2 = bin2 % 10
            sum = binary1 + binary2 + carry
            if sum > 2:
                carry = 1
                ans = '1' + ans
            elif sum > 1:
                carry = 1
                ans = '0' + ans
            else:
                carry = 0
                ans = str(sum) + ans
            bin1 //= 10
            bin2 //= 10
        if carry:
            return '1' + ans
        else:
            return ans