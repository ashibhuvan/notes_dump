# Best Time to Buy and Sell Stock Memoization Version
class Solution
    def maxProfit(self, prices: List[nums]) -> int:
        memo = {}
        def dfs(start: int) -> int:
            if start >= len(prices):
                return 0
            if start in memo:
                return memo[start]
            max_profit = 0
            for i in range(start, len(prices):
                    profit = prices[i] - prices[start] + dfs(i + 1)
                    max_profit = max(max_profit, profit)
            memo[start] = max_profit
            return max_profit

        return dfs(0)
