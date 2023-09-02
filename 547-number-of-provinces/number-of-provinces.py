class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        print(adj)

        vis = [0]*n
        ans = 0

        def dfs(node):
            vis[node] = 1
            for item in adj[node]:
                if vis[item] == 0:
                    dfs(item)

        for i in range(n):
            if vis[i] == 0:
                ans += 1
                dfs(i)

        return ans