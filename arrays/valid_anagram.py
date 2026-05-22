# Problem: Valid Anagram
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Count frequency of characters using hashmap.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Forgetting to check string lengths before counting characters.

# Revision Note:
# Can also be solved using sorting.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT