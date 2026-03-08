class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        setStr={num for num in nums}

        def backtrack(ind,curStr):
            
            if ind == len(nums):
                res= "".join(curStr)
                if res not in setStr: return res
                return None
            
            res = backtrack(ind+1,curStr+"0")
            if res : return res
            res = backtrack(ind+1,curStr+"1")
            if res : return res
                
            

            

            
        return backtrack(0,"")
