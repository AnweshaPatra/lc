class Solution:
    def eventualSafeNodes(self, adj: List[List[int]]) -> List[int]:
        n = len(adj)
        '''
        #DFS using visited, path visited lists
        vis = [0]*v
        pvis = [0]*v
        check = [0]*v
        safeNodes = []

        def dfs(node):
            vis[node] = 1
            pvis[node] = 1
            check[node] = 0
            for item in adj[node]:
                if vis[item] == 0:
                    if dfs(item) == True:
                        check[node] = 0
                        return True
                elif pvis[item] == 1:
                    check[node] = 0
                    return True
            check[node] = 1
            pvis[node] = 0
            return False

        for i in range(v):
            if vis[i] == 0:
                dfs(i)

        for i in range(v):
            if check[i] == 1:
                safeNodes.append(i)

        return safeNodes
        '''
        #BFS using topological sort 
        #convert the adjacency matrix, basically the directions of the edges in the opposite direction
        adjRev = [[] for _ in range(n)]
        indegree = [0]*n
        for i in range(n):
            for item in adj[i]:
                adjRev[item].append(i)
                indegree[i] += 1
        queue = []
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        print(adjRev)
        topo = []
        while len(queue) != 0:
            node = queue.pop(0)
            topo.append(node)
            for item in adjRev[node]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    queue.append(item)
        
        topo.sort()
        return topo
            
        