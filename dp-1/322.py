class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp_cache = [amount+1] * (amount+1)
        dp_cache[0] = 0
        # bottom up DP 
        for i in range(1, amount+1):
            for c in coins:
                # if valid num
                if i - c >= 0:
                    dp_cache[i] = min(dp_cache[i], 1+dp_cache[i-c])
        
        if dp_cache[amount] != amount +1:
            return dp_cache[amount]

        return -1