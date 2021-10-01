class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2): # make len1 > len2
            tmp = num2
            num2 = num1
            num1 = tmp
        if len(num1) > len(num2):    
            num2 = "0" * (len(num1) - len(num2)) + num2
        carry = 0
        res = []
        for i in range(len(num1)):
            tmp_sum = int(num1[len(num1) - i - 1]) + int(num2[len(num1) - i - 1]) + carry
            rem = tmp_sum % 10
            carry = tmp_sum // 10
            res.append(str(rem))
        if carry == 1:
            res.append(str(carry))
        string = ''.join(res[::-1])
        return string