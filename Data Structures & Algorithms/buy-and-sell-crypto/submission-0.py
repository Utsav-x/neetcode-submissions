class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        leng = len(prices)
        for i in range(leng):
            for j in range(leng):
                
                if i < j:
                    print(prices[i],prices[j])
                    prof = prices[j] - prices[i]
                    maxprofit = max(maxprofit,prof)
        
        return maxprofit