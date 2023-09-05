class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1]*n

        def dfs(node, c):
            color[node] = c
            for item in graph[node]:
                if color[item] == -1:
                    if dfs(item, int(not c)) == False: return False
                elif color[item] == c:
                    return False
            return True
        
        for i in range(n):
            if color[i] == -1:
                if dfs(i, 0) == False:
                    return False
        return True
        