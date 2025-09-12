class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp_cache = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        # 1 way to sum to zero
        for i in range(len(coins) + 1):
            dp_cache[i][0] = 1
        
        for i in range(len(coins) - 1, -1, -1):
            # goes from 0 -> 5 0,1,2,3,4,5
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp_cache[i][a] = dp_cache[i + 1][a]
                    dp_cache[i][a] += dp_cache[i][a - coins[i]]

        return dp_cache[0][amount]