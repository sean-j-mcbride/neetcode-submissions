class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def rotFruit(r, c):
            if (r not in range(ROWS) or c not in range(COLS) or
                (r, c) in visit or grid[r][c] == 0):
                return
            q.append([r, c])
            visit.add((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
        
        time = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                rotFruit(r + 1, c)
                rotFruit(r - 1, c)
                rotFruit(r, c + 1)
                rotFruit(r, c - 1)
            time += 1
        
        print(time)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time - 1 if time > 0 else 0
                
            