class Solution:
    def processStr(self, s: str) -> str:
        res=""

        for ch in s:
            if ch=="*" and s:
                res=res[:-1]
            
            elif ch=="#":
                res=res*2
            elif ch=="%":
                res=res[::-1]
            else:
                res+=ch
        return res