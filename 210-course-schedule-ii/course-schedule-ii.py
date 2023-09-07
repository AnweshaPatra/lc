class Solution:
    def findOrder(self, num: int, prereq: List[List[int]]) -> List[int]:
        #asking for the topological ordering is it doesn't have a cycle otherwise we return empty list if it does contain a cycle
        n = len(prereq)
        adj = [[] for _ in range(num)]
        def adjacent(i, j):
            adj[i].append(j)
            return adj

        for i in range(n):
            u = prereq[i][0]
            v = prereq[i][1]
            adj = adjacent(u, v)
    
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
            return topo[::-1]
        return []

        