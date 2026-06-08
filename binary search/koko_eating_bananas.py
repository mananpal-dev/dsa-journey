# Problem: Koko Eating Bananas
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Binary Search on Answer.
# Search for the minimum eating speed k such that
# Koko can finish all bananas within h hours.
#
# For a given speed:
# hours_needed = sum(ceil(pile / speed))
#
# If hours_needed <= h:
# speed works, try a smaller one.
#
# Otherwise:
# speed is too slow, try a larger one.

# Time Complexity: O(n log m)
# n = number of piles
# m = max(piles)

# Space Complexity: O(1)

# Common Mistake:
# Using pile // speed instead of ceil(pile / speed).
#
# Example:
# pile = 7, speed = 4
#
# 7 // 4 = 1   ❌
# ceil(7 / 4) = 2 ✅
#
# Use:
# (pile + speed - 1) // speed

# Revision Note:
# Binary Search on Answer pattern.
#
# left  = minimum possible speed = 1
# right = maximum possible speed = max(piles)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        answer = right

        while left <= right:

            speed = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += (pile + speed - 1) // speed

            if hours <= h:

                answer = speed
                right = speed - 1

            else:

                left = speed + 1

        return answer