class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [1]*(n+1)
        if n < 2:
            return n
        arr[0] = 0
        arr[1] = 1
        arr[2] = 1
        for i in range(3,n+1):
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
        return arr[n]
print(Solution().tribonacci(5))