class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        if not grid:
            return 0
        row, col, visited, island = len(grid), len(grid[0]), set(), 0

        def bfs(r, c):
            q=[]
            q.append([r, c])
            visited.add((r, c))
            while q :
                rows,cols = q.pop()
                direction = [[-1,0],[1,0],[0,1],[0,-1]]
                for dr, dc in direction:
                    r,c = rows+dr, cols+dc
                    if ((c in range(col)) and 
                    (r in range(row)) and 
                    ((r,c) not in visited) and
                    grid[r][c] == "1"):
                        q.append([r,c])
                        visited.add((r,c))
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    island += 1
        return island
    # def numIslands(self, grid):
    #     seen = []
    #     direct = [[1,0], [-1, 0], [0, 1], [0, -1]]
    #     def bfs(r, c):
    #         if [r, c] in seen:
    #             return
    #         q = [[r, c]]
    #         while q:
    #             rows, cols = q.pop(0)
    #             for i in  direct:

    #                 if [r, c] not in seen and (r in range(row)) and (c in range(col)):

            
    #     count = 0
    #     row = len(grid)
    #     col = len(grid[0])
    #     for r in range(row):
    #         for c in range(col):
    #             if grid[r][c] == '1':
    #                 bfs(r, c)
    #                 count += 1
    #     return count
    
print(Solution().numIslands(
  [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

print(Solution().numIslands(
 [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
))
