from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxx = 0

        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            length = 1

            while q:
                row, col = q.popleft()
                directions = [[0,1], [1,0], [-1,0], [0,-1]]

                for dr,dc in directions:
                    r,c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == 1 and 
                    (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                        length+=1

            return length

                    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    length = bfs(r,c)
                    maxx = max(maxx,length)
        return maxx
                    


        