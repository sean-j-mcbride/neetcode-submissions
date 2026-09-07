class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rotten = set()
        isFresh = False

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.add((r, c))
                elif grid[r][c] == 1:
                    isFresh = True
        
        if not rotten and not isFresh:
            return 0

        mins = 0

        while rotten:
            newRotten = set()
            mins += 1
            for rotR, rotC in rotten:

                for dr, dc in directions:
                    nr, nc = rotR + dr, rotC + dc

                    if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0 or grid[nr][nc] == 2):
                        continue
                    
                    grid[nr][nc] = 2
                    newRotten.add((nr, nc))
            
            rotten = newRotten.copy()
        mins -= 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return mins

