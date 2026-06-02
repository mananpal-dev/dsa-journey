# Problem: Best Time to Buy and Sell Stock
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Track the lowest buying price seen so far.
# For each day, calculate the profit if sold today.
# Keep updating the maximum profit.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Common Mistake:
# Updating profit before checking whether the
# current price is a new minimum buy price.

# Revision Note:
# Fundamental Sliding Window / Two Pointers pattern.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:

            if buy_price > p:
                buy_price = p

            profit = max(profit, p - buy_price)

        return profit