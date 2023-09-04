class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        visited = [[0]*m for _ in range(n)]
        distance = [[-1]*m for _ in range(n)]
        queue = []
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append([i, j, 0])

        while len(queue) != 0:
            node = queue.pop(0)
            row = node[0]
            col = node[1]
            step = node[2]
            visited[row][col] = 1
            distance[row][col] = step

            for k in range(4):
                nrow = row + drow[k]
                ncol = col + dcol[k]
                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and mat[nrow][ncol] == 1 and visited[nrow][ncol] == 0:
                    visited[nrow][ncol] = 1
                    queue.append([nrow, ncol, step + 1])
        
        return distance
            