class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxprofit=0
        minstake=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minstake:
                minstake=prices[i]
            else:
                if prices[i]-minstake>mxprofit:
                    mxprofit=prices[i]-minstake
        return mxprofit