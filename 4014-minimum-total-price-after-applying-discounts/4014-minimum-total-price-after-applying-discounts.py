class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        res=0
        curInd=0
        while curInd<len(prices) and curInd<len(discounts):
            finalPrice=prices[curInd]*((100-discounts[curInd])/100)
            res+=finalPrice
            curInd+=1
        
        res+=sum(prices[curInd:])
        
        return res