# class Solution:
#     def minCostClimbingStairs(self, cost) -> int:
#         n = len(cost)
#         dp = [0] * n
#         dp[0] = cost[0]
#         dp[1] = cost[1]
#         dp[3] = cost[3]
#         for i in range(2,n):
#             dp[i] = min(dp[i-1], dp[i-2], dp[i-3]) + cost[i]
#         print(dp)
#         return min(dp[n-1],dp[n-2], dp[n-3])
# print(Solution().minCostClimbingStairs([1,2,3,4,5,6,7]))

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            cost_from_i = cost[i] + min(dfs(i+1), dfs(i+2))
            memo[i] = cost_from_i
            return cost_from_i

        return min(dfs(0), dfs(1))


# Example usage
print(Solution().minCostClimbingStairs([10, 15, 20])) 
