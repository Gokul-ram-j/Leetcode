class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sm=0
        maxSum=float('-inf')
        for val in nums:
            sm+=val
            maxSum=max(sm,maxSum)

            if sm<0:
                sm=0
        return maxSum