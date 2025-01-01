class Solution:
    def mincostTickets(self, days, cost):
        memory = {}
        def dfs(i):
            if i >= len(days):
                return 0
            if i in memory:
                return memory[i]
            # Find the next index for 7-day and 30-day passes
            j = i
            while j < len(days) and days[j] <= days[i] + 6:
                j += 1
            
            k = i
            while k < len(days) and days[k] <= days[i] + 29:
                k += 1
            
            # Calculate the minimum cost
            sums =  min(
                dfs(i + 1) + cost[0],  # 1-day pass
                dfs(j) + cost[1],      # 7-day pass
                dfs(k) + cost[2]       # 30-day pass
            )
            memory[i] = sums
            return sums
        
        return dfs(0)

# Example usage
obj = Solution()
print(obj.mincostTickets(days=[1, 4, 6, 7, 8, 20], cost=[2, 7, 15]))  # Output: 11


class Solution:
    def mincostTickets(self, days, cost):
        # Create a set of travel days for fast lookup
        day_set = set(days)
        # Create a dp array where dp[i] represents the minimum cost up to day i
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        
        for i in range(1, last_day + 1):
            if i not in day_set:
                # If it's not a travel day, cost remains the same as the previous day
                dp[i] = dp[i - 1]
            else:
                # Take the minimum of the three ticket costs
                dp[i] = min(
                    dp[i - 1] + cost[0],  # 1-day pass
                    dp[i - 7] + cost[1] if i >= 7 else cost[1],  # 7-day pass
                    dp[i - 30] + cost[2] if i >= 30 else cost[2]  # 30-day pass
                )
        print(dp)
        # The answer is the minimum cost to cover all travel days
        return dp[last_day]

# Example usage
obj = Solution()
print(obj.mincostTickets(days=[1, 4, 6, 7, 8, 20], cost=[2, 7, 15]))  # Output: 11
