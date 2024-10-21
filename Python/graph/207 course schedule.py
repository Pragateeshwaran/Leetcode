class Solution:
    def canFinish(self, numCourses: int, pre) -> bool:
        
        course = { i : [] for i in range(numCourses)}
        print(course)
        for i,j in pre:
            course[i].append(j)
        visitset = set()
        print(course)
        def dfs(i):
            if i in visitset:
                return False
            if course[i] == []:
                return True
            visitset.add(i)
            for j in course[i]:
                if not dfs(j):
                    return False
            visitset.remove(i)
            course[i] = []
            return True
        for i in course:
            if not dfs(i):
                return False
        return True

print(Solution().canFinish(numCourses = 2, pre = [[1,0]]))
print(Solution().canFinish(numCourses = 2, pre = [[1,0],[0,1]]))