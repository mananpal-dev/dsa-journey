# Problem: Product of Array Except Self
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# First pass stores prefix (left) products.
# Second pass multiplies postfix (right) products.

# Time Complexity: O(n)
# Space Complexity: O(1) extra space

# Common Mistake:
# Updating prefix/postfix before storing value
# causes incorrect multiplication order.

# Revision Note:
# Important Prefix & Postfix product pattern.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prefix = 1

        # Store left products
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        # Multiply right products
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res