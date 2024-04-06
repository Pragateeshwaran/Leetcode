class Solution:
    def generate(self, numRows: int):

        ans=[[1]]
        for _ in range(2,numRows+1):

            row = [ans[-1][i]+ans[-1][i+1] for i in range(len(ans[-1])-1) ]
            row = [1]+row+[1]
            ans.append(row)

        return ans
print(Solution().generate(5))
