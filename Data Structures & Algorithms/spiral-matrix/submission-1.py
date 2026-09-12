class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        while matrix and matrix[0]:
            for x in matrix[0]:
                res.append(x)

            if len(matrix) > 2:
                for i in range(1, len(matrix) - 1):
                    res.append(matrix[i][-1])

            if len(matrix) > 1:
                for i in range(1, len(matrix[0]) + 1):
                    res.append(matrix[-1][-i])

            if len(matrix) > 2 and len(matrix[0]) > 1:
                for i in range(2, len(matrix)):
                    res.append(matrix[-i][0])
            
            matrix = [row[1:-1] for row in matrix[1:-1]]
        return res
