class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        paths = {i: [] for i in range(n)}
        for i, j in edges:
            paths[i].append(j)
            paths[j].append(i)
        print(paths)
        def dfs(i):
            if i == destination:
                return True
            visited.add(i)
            for edge in paths[i]:
                if edge not in visited and dfs(edge):
                    return True
            return False

        visited = set()
        return dfs(source)
print(Solution().validPath(n = 4, edges = [[0,1],[1,2],[2,3],[3,1]], source = 0, destination = 3))