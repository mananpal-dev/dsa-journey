# Problem: Valid Sudoku
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use hash sets to track numbers in rows,
# columns, and 3x3 squares.

# Time Complexity: O(1)
# Space Complexity: O(1)

# Common Mistake:
# Forgetting to skip '.' empty cells.

# Revision Note:
# Important HashSet validation pattern.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True