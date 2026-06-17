# Problem: Remove Duplicates from Sorted Array
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Use Two Pointers.
#
# i -> points to the last unique element.
# j -> scans the array.
#
# Whenever a new unique element is found,
# move i forward and place the new element at nums[i].
#
# The first (i + 1) elements will contain all unique values.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Common Mistake:
# Forgetting to return i + 1.
# i stores the index of the last unique element,
# so the number of unique elements is i + 1.

# Revision Note:
# Slow Pointer (i) -> Last unique element.
# Fast Pointer (j) -> Traverse the array.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0

        for j in range(1, len(nums)):

            if nums[j] != nums[i]:

                i += 1
                nums[i] = nums[j]

        return i + 1