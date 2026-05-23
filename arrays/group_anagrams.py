# Problem: Group Anagrams
# Platform: LeetCode
# Difficulty: Medium

# Approach 1:
# Sort each string and use it as hashmap key.
# Anagrams will have same sorted string.

# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)

# Common Mistake:
# Forgetting to convert sorted list back into string using join().

# Revision Note:
# Later revise frequency count optimization approach.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for s in strs:

            key = "".join(sorted(s))

            ans[key].append(s)

        return list(ans.values())


# --------------------------------------------------


# Optimized Approach:
# Use character frequency count as hashmap key.

# Time Complexity: O(n * k)
# Space Complexity: O(n * k)

# Common Mistake:
# Forgetting lists cannot be used as dictionary keys.
# Convert count list into tuple.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for s in strs:

            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            ans[tuple(count)].append(s)

        return list(ans.values())