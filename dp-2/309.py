class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def _dfs(i, buy):
            # if buy:
            #     print(i,"buy")
            # else:
            #     print(i,"sell")
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i,buy)]
            
             
            cool_price = _dfs(i+1, buy)
            
            # if we need to buy stock
            if buy:
                buy_price = _dfs(i+1, False) - prices[i]
                dp[(i,buy)] = max(buy_price, cool_price)
            else:
                sell_price = _dfs(i+2, True) + prices[i]
                dp[(i,buy)] = max(sell_price, cool_price)
            
            return dp[(i,buy)]
        
        return _dfs(0,True)