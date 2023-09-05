class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        def check(start):
            queue = []
            queue.append(start)
            color[start] = 0
        
            while len(queue) != 0:
                node = queue.pop(0)
                for item in graph[node]:
                    if color[item] == -1:
                        color[item] = int(not color[node])
                        queue.append(item)
                    elif color[item] != -1:
                        if color[item] == color[node]:
                            return False
            return True
        
        color = [-1]*n
        for i in range(n):
            if color[i] == -1:
                if check(i) == False:
                    return False
        return True
        