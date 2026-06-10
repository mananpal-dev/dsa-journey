# Problem: Remove Duplicates from Sorted Array II
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Count occurrences while traversing the array.
# Allow each number to appear at most twice.
# Overwrite valid elements in-place using pointer k.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Forgetting that the array must be modified in-place.
# Returning a new array will not satisfy the problem requirements.

# Revision Note:
# Use k to track the next position where
# a valid element should be written.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count = {}
        k = 0

        for num in nums:

            count[num] = count.get(num, 0) + 1

            if count[num] <= 2:
                nums[k] = num
                k += 1

        return k