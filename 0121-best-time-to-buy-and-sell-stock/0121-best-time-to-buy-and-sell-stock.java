import java.util.List;

class Solution {
    public int maxProfit(int[] prices) {
        int mxprofit = 0;
        int minstake = prices[0];
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < minstake) {
                minstake = prices[i];
            } else if (prices[i] - minstake > mxprofit) {
                mxprofit = prices[i] - minstake;
            }
        }
        return mxprofit;
    }
}