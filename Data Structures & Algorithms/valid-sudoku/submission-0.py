class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # A single hash set to store all seen number-position combinations.
        seen = set()

        # Iterate through each cell of the 9x9 board.
        for r in range(9):
            for c in range(9):
                num = board[r][c]

                # Ignore empty cells.
                if num == ".":
                    continue

                # Create unique string identifiers for the number in its row, col, and box.
                row_key = f"row {r} has {num}"
                col_key = f"col {c} has {num}"
                box_key = f"box {r//3}-{c//3} has {num}"

                # Check if we've seen this number in this row, col, or box before.
                if row_key in seen or col_key in seen or box_key in seen:
                    return False # Found a duplicate.

                # If no duplicate, add these new facts to our set.
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        # If we get through the whole board without finding duplicates, it's valid.
        return True
