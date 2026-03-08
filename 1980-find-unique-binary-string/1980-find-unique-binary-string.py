class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        setStr={num for num in nums}

        def backtrack(ind,curStr):
            
            if ind == len(nums):
                res= "".join(curStr)
                return None if res in setStr else res
                
            res= backtrack(ind+1,curStr)
            if res : return res

            curStr[ind]="1"
            res= backtrack(ind+1,curStr)
            if res : return res

            
        return backtrack(0,["0" for _ in nums])
