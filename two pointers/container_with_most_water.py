# Problem: Container With Most Water
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use two pointers at both ends of the array.
# Calculate area and move the pointer with the smaller height.
# This gives a chance to find a taller line and potentially larger area.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Common Mistake:
# Moving the taller pointer instead of the shorter one.
# The shorter height is always the limiting factor.

# Revision Note:
# Classic Two Pointers optimization problem.

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        maxArea = 0

        while left < right:

            maxArea = max(
                maxArea,
                (right - left) * min(height[left], height[right])
            )

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea