class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]

        
        def backtrack(s,openCnt,closeCnt):
            if len(s)==n*2 :
                res.append(s)
                return
            
            if openCnt<n:
                backtrack(s+'(',openCnt+1,closeCnt)

            if closeCnt<openCnt:
                backtrack(s+')',openCnt,closeCnt+1)
        
        backtrack("",0,0)

        return res