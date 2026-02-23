class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total=sum(nums)
        curSum=0

        for i in range(len(nums)):
            curSum+=nums[i]
            rightSum=total-curSum
            leftSum=curSum-nums[i]

            if rightSum==leftSum: return i
        
        return -1

