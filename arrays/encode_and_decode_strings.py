# Problem: Encode and Decode Strings
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Store length of string followed by delimiter '#'.
# While decoding, read length first and then extract string.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Forgetting to move pointer after '#'
# while decoding.

# Revision Note:
# Important String Encoding technique.

class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res


    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):

            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            res.append(s[j + 1:j + 1 + length])

            i = j + 1 + length

        return res