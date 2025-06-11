# basic sliding window https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        max_profit = 0
        end = start + 1

        if len(prices) <= 1:
            return 0
        
        while end < len(prices):
            max_profit = max(max_profit, prices[end] - prices[start])

            if prices[start] > prices[end]:
                start = end
            else:
                end += 1
        
        return max_profit
