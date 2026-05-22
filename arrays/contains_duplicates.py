# Problem: Contains Duplicate
# Platform: LeetCode
# Difficulty: Easy

# Approach 1:
# Compare length of list with length of set.
# If lengths differ, duplicate exists.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Forgetting that set removes duplicate values automatically.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# --------------------------------------------------


# Approach 2:
# Sort the array and compare adjacent elements.

# Time Complexity: O(n log n)
# Space Complexity: O(1)

# Common Mistake:
# Forgetting to check nums[i] with nums[i + 1].

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False


# --------------------------------------------------


# Approach 3:
# Use a hash set to track visited elements.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Forgetting to add elements into the set after checking.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False