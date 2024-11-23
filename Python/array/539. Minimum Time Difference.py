class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        vec = []
        for timePoint in timePoints:
            h, m = map(int, timePoint.split(':'))
            mins = h * 60 + m
            vec.append(mins)
        vec.sort()
        
        res = float('inf')
        for i in range(1, len(vec)):
            res = min(vec[i] - vec[i - 1], res)
        
        return min(res, 1440 + vec[0] - vec[-1])
    
print(Solution().findMinDifference(timePoints = ["23:59","00:00"]))
print(Solution().findMinDifference( timePoints = ["00:00","23:59","00:00"]))
