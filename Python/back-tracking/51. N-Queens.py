class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        diagonals1 = set()
        diagonals2 = set()
        cols = set()
        res = []
        board = [['.']*n for _ in range(n)]
        def dfs(row):
            if row == n:
                res.append([''.join(rows) for rows in board])
                return
            
            for col in range(n):
                if col not in cols and row - col not in diagonals1 and row + col not in diagonals2:
                    board[row][col] = 'Q'
                    cols.add(col)
                    diagonals1.add(row - col)
                    diagonals2.add(row + col)

                    dfs(row + 1)
                    
                    board[row][col] = '.'
                    cols.remove(col)
                    diagonals1.remove(row - col)
                    diagonals2.remove(row + col)

        dfs(0)
        print(board)
        return res

print(Solution().solveNQueens(4))