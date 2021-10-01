class Solution:
    # Approach 1:
    def addBinary(self, a: str, b: str) -> str:
        if (len(a) < len(b)): # make sure len(a) >= len(b)
            tmp = b
            b = a
            a = tmp
        if (len(a) > len(b)):
            b = "0" * (len(a) - len(b)) + b
        carry = 0
        res = []
        for i in range(len(a)):
            if a[len(a)-i-1] == "1" and b[len(a)-i-1] == "1":
                if carry == "1":
                    res.append("1") 
                else:
                    res.append("0") 
                carry = "1"
            elif a[len(a)-i-1] != b[len(a)-i-1]:
                if carry == "1":
                    res.append("0") 
                    # carry = "1"
                else:
                    res.append("1") 
                    # carry = "0"
            else:
                if carry == "1":
                    res.append("1") 
                else:
                    res.append("0")
                carry = "0"
        if carry == "1":
            res.append("1") 
        string = ''.join(res[::-1])
        return string
    
    # Approach 2:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)==0: return b
            if len(b)==0: return a
            if a[-1] == '1' and b[-1] == '1':
                return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
            if a[-1] == '0' and b[-1] == '0':
                return self.addBinary(a[0:-1],b[0:-1])+'0'
            else:
                return self.addBinary(a[0:-1],b[0:-1])+'1'