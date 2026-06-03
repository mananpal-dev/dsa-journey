# Problem: Longest Repeating Character Replacement
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use a sliding window and track character frequencies.
# Keep expanding the window while the number of
# replacements needed is at most k.
# If replacements exceed k, shrink the window.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Common Mistake:
# Forgetting that:
# window_length - max_frequency
# gives the replacements needed.

# Revision Note:
# Window is valid when:
# window_length - max_frequency <= k

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        left = 0
        max_freq = 0
        res = 0

        for right in range(len(s)):

            count[s[right]] = 1 + count.get(s[right], 0)

            max_freq = max(max_freq, count[s[right]])

            while (right - left + 1) - max_freq > k:

                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res