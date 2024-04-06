class Solution:
    def nearestExit(self, maze, entrance) -> int:
        rows,columns = len(maze),len(maze[0])

        dir = [[1,0],[-1,0],[0,1],[0,-1]]


        q = [(*entrance,0)]
        maze[entrance[0]][entrance[1]] = '+'
        print("------>",maze)

        while q:
            r,c,step = q.pop(0)
          
            if (min(r,c)==0 or r == rows-1 or c == columns-1) and [r,c] != entrance:
                return step
            for d in dir:
                r1 = r+d[0]    
                c1 = c+d[1]
                if 0<=r1<rows and 0<=c1<columns and maze[r1][c1]=='.' :
                    maze[r1][c1] = '+'
                    q.append([r1,c1,step+1])
                    
        return -1
print(Solution().nearestExit(maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]))
print(Solution().nearestExit(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]))
print(Solution().nearestExit(maze = [[".","+"]], entrance = [0,0]))
