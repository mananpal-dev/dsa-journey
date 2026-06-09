# Problem: Find Minimum in Rotated Sorted Array
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use Binary Search.
# Compare the middle element with the rightmost element.
#
# If nums[mid] <= nums[right]:
# the minimum lies in the left half (including mid).
#
# Otherwise:
# the minimum lies in the right half.
#
# Keep shrinking the search space until
# left == right.

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Common Mistake:
# Using right = mid - 1 when nums[mid] <= nums[right].
# Mid itself could be the minimum, so use:
# right = mid

# Revision Note:
# In a rotated sorted array,
# one half is always sorted.
# Use nums[mid] and nums[right]
# to determine where the minimum lies.

class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] <= nums[right]:
                right = mid

            else:
                left = mid + 1

        return nums[left]