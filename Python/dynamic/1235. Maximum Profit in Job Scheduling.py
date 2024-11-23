class Solution:
    def jobScheduling(self, startTime: [int], endTime: [int], profit: [int]) -> int:
        events = sorted(zip(startTime, endTime, profit))
        print(events)
        cache = {}
        def dfs(i):
            if i >= len(events):
                return 0
            nonlocal cache
            if i in cache:
                return cache[i]
            
            res = dfs(i+1)
            j = i
            while j < len(events):
                if events[i][1] <= events[j][0]:
                    break
                j+= 1
            res = max(res, dfs(j)+events[i][2])
            cache[i] = res 
            print(cache)
            return res
        return dfs(0)


startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]
sol = Solution()
result = sol.jobScheduling(startTime, endTime, profit)
print(result)