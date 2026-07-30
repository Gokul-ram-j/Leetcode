class Solution:
    def myAtoi(self, s: str) -> int:


        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        def cti(s):
            num = 0
            for ch in s:
                num = num * 10 + (ord(ch) - ord('0'))
            return num
                
        res=""
        sign=""
        s=s.lstrip()
        for i in range(len(s)):
            if s[i].isalpha() or s[i]=='.' or s[i]==" ":
                break
            elif s[i].isdigit():
                res+=s[i]
            elif s[i]=='-' or s[i]=='+':
                if res or sign : break
                sign=s[i]
        
        num = cti(res)
        if sign == '-':
            num = -num

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num

       