class Solution:
    def getRow(self, n: int):
        rowIndex = [[1]]
        for _ in range(1,n+1):
            row = [rowIndex[-1][i] + rowIndex[-1][i+1] for i in range(0, len(rowIndex[-1])-1)]
            row = [1] + row + [1]
            rowIndex.append(row)
        return rowIndex[n]

print(Solution().getRow(5))