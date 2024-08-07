class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        brute force : compare all differences
        optimal : two pointer approach with a left and right pointer
        left - where you buy, right - where you sell
        move left to a non negative profit
        then right to maximize profit

        '''
        maxprofit = 0
        left = 0
        right = 1
        while (right < len(prices)):
            profit = prices[right] - prices[left]
            if profit < 0:
                left += 1
                right = left + 1
            else:
                if profit > maxprofit:
                    maxprofit = profit
                right += 1
        
        return maxprofit