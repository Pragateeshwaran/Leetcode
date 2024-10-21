class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:  
            l, r = 0, len(row) - 1  

            while l <= r:  
                row[l], row[r] = 1 - row[r], 1 - row[l]
                l += 1  
                r -= 1  

        return image

print(Solution().flipAndInvertImage(image = [[1,1,0],[1,0,1],[0,0,0]]))
print('\n')
print(Solution().flipAndInvertImage(image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
print('\n')
print(Solution().flipAndInvertImage([[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]))
