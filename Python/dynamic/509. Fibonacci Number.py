class Solution:
    def fib(self, n: int) -> int:
        arr = [0]*(n+1)
        if n < 2:
            return n
        else:
            arr[0] = 0 
            arr[1] = 1
        for i in range(2,n+1):
            arr[i] = arr[i-1] + arr[i-2]
        print(arr)
        return arr[n]
    
print(Solution().fib(n=3))


