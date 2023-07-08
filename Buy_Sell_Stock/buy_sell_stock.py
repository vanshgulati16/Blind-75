class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 # left pointer will give us buying prices
        j = 1 # right pointer will give us selling price
        profit = 0 #Max profit 
        while(j<len(prices) ):
            # storing current profit(if it is negative also we are storing it here)
            curr_profit = prices[j] - prices[i]
            # we will have profit if BP is less than SP
            if prices[i]<prices[j] :
                # now we will assign the max profit(by checking pervious and current profit) in profit
                profit = max(curr_profit, profit)
            # if bp is greater or equal to SP we shift left to right
            else:
                i=j
            # and always increment right pointer by 1 for checking max profit
            j+=1
        return profit