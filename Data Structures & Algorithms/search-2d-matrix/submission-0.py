class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        target_row = []

        while l <= r and not target_row:
            mid = l + ((r-l) // 2)

            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                target_row = matrix[mid]
        
        if not target_row:
            return False

        l, r = 0, len(target_row) - 1

        while l <= r:
            mid = l + ((r-l) // 2)

            if target < target_row[mid]:
                r = mid - 1
            elif target > target_row[mid]:
                l = mid + 1
            else:
                return True
        
        return False