class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        res=[-1,-1]
        curInd=0

        while(curInd<len(nums)):
            if nums[curInd]==target:
                res[0]=curInd
                break
            curInd+=1

        curInd=len(nums)-1

        while(curInd>=0):
            if nums[curInd]==target:
                res[-1]=curInd
                break
            curInd-=1
        
        return res



        