class Solution:
    def canFinish(self, num: int, prereq: List[List[int]]) -> bool:
        n = len(prereq)

        adj = [[] for _ in range(num)]

        def adjacent(i, j):
            adj[i].append(j)
            return adj

        for i in range(n):
            u = prereq[i][0]
            v = prereq[i][1]
            adj = adjacent(u, v)
        '''
        #DFS
        vis = [0]*num
        pvis = [0]*num

        def dfs(node):
            vis[node] = 1
            pvis[node] = 1
            if len(adj[node]) > 0:
                for item in adj[node]:
                    if vis[item] == 0:
                        if dfs(item) == True:
                            return True
                    elif pvis[item] == 1:
                        return True
            return False

        for i in range(num):
            if dfs(i) == True:
                return True
        return False
        '''

        #BFS using topological sort Kahn's Algorithm
        indegree = [0]*num
        for i in range(num):
            if len(adj[i]) > 0:
                for item in adj[i]:
                    indegree[item] += 1
        
        queue = []
        for i in range(num):
            if indegree[i] == 0:
                queue.append(i)
        
        topo = []

        while len(queue) != 0:
            node = queue.pop(0)
            topo.append(node)
            for item in adj[node]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    queue.append(item)
        
        if len(topo) == num:
            return True
        return False