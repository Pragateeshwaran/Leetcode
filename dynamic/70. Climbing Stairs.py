"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45"""

class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1] * (n+1)
        for i in range(2,n+1):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n]
print(Solution().climbStairs(38))



class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        def helper(i):
            nonlocal count
            if i == n:
                count += 1
                return
            if i > n:
                return
            helper(i+1)
            helper(i+2)
        helper(0)
        return count

print(Solution().climbStairs(38))



class Solution:
    def climbStairs(self, n: int) -> int:
        diction = {}  
        def dfs(i):
            if i > n:
                return 0 
            if i == n:
                return 1 
            if i in diction:
                return diction[i] 
            count = dfs(i + 1) + dfs(i + 2)
            diction[i] = count
            return count

        return dfs(0)
