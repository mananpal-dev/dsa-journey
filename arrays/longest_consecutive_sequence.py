# Problem: Longest Consecutive Sequence
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Store numbers in a set for O(1) lookup.
# Start sequence only if previous number does not exist.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Starting sequence from every number
# instead of only sequence starters.

# Revision Note:
# Important Set optimization pattern.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for n in numSet:

            if (n - 1) not in numSet:

                length = 1

                while (n + length) in numSet:
                    length += 1

                longest = max(length, longest)

        return longest