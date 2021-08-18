# Best Time to Buy and Sell Stock with Cooldown

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:

# Input: prices = [1]
# Output: 0
 

# Constraints:

# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.profit(prices, 0, {})
    def profit(self, prices, cur, mem):
        if cur >= len(prices):
            return 0
        
        if cur in mem:
            return mem[cur]
        
#         we can sell or cur or we can't sell
        
        maximum = 0
        # lets see for selling at current
        cur_price = prices[cur]
        for i in range(cur+1, len(prices)):
            price = prices[i]
            if cur_price < price:
                # sell or not sell current stock at ith day
                maximum = max(maximum, price - cur_price + self.profit(prices, i+2, mem))
        
        # let see if we can sell cur stock
        maximum = max(maximum, self.profit(prices, cur+1, mem))
        mem[cur] = maximum
        return maximum