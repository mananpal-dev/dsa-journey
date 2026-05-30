# Problem: Two Sum II - Input Array Is Sorted
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Since the array is sorted, use two pointers.
# If sum is too large, move right pointer left.
# If sum is too small, move left pointer right.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Common Mistake:
# Forgetting that the problem requires
# 1-indexed positions in the answer.

# Revision Note:
# Fundamental Two Pointers problem.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:

            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]

            elif total > target:
                right -= 1

            else:
                left += 1