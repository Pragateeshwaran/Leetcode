class Solution:
    def findCircleNum(self, isConnected) -> int:
        graph = {}
        for i in range(1, 1 + len(isConnected)):
            graph[i] = []
            for j in range(1, 1 + len(isConnected[i - 1])):
                if isConnected[i - 1][j - 1] == 1 and i != j:
                    graph[i].append(j)
        print(graph)
        seen = []
        def dfs(root):
            if root in seen:
                return
            seen.append(root)
            for neighbour in graph[root]:
                dfs(neighbour)
        res = 0
        for i in graph:
            if i not in seen:
                res+=1
                dfs(i)
        return res
solution = Solution()
solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])

print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))