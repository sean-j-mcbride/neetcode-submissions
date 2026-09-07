class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF, ROWS, COLS = 2147483647, len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        dist = 0
        while q:
            dist += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS
                            or grid[nr][nc] != INF):
                        continue
                    grid[nr][nc] = dist
                    q.append((nr, nc))