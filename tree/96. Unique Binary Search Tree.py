class Solution:
    def numTrees(self, n: int) -> int:
        num = [1]*(n+1)
        for i in range(2, n+1):
            total = 0
            for j in range(1,i+1):
                left = j -1
                right = i -j
                print("left-------->",num[left])
                print("right-------->",num[right])
                total += num[left]*num[right]
                print("total    :",total)
                print('no of resolution         :',i)
            num[i] = total
            print(num)
        
        return num[n]


print(Solution().numTrees(19))