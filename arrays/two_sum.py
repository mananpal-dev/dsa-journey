# Problem: Two Sum
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Brute Force using nested loops.
# Check every pair and return indices if target is found.

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Common Mistake:
# Forgetting to return [i, j] instead of only return statement.

# Revision Note:
# Later revise optimized HashMap approach.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i, j]
                
# --------------------------------------------------


# Optimized Approach:
# Use HashMap to store previously visited numbers.
# Check whether required complement already exists.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Storing current element before checking complement
# may lead to using same index twice.

# Revision Note:
# Important pattern for HashMap problems.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMap = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in numMap:
                return [numMap[complement], i]

            numMap[nums[i]] = i

        return []