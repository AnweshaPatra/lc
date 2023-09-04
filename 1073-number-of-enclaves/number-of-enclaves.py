class Solution:
    def numEnclaves(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        visited = [[0]*m for _ in range(n)]
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        def dfs(i, j):
            visited[i][j] = 1
            row = i
            col = j
            for k in range(4):
                nrow = row + drow[k]
                ncol = col + dcol[k]
                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and visited[nrow][ncol] == 0 and mat[nrow][ncol] == 1:
                    dfs(nrow, ncol)
        
        for j in range(m):
            if mat[0][j] == 1 and visited[0][j] == 0:
                dfs(0, j)
            if mat[n-1][j] == 1 and visited[n-1][j] == 0:
                dfs(n-1, j)
        for i in range(n):
            if mat[i][0] == 1 and visited[i][0] == 0:
                dfs(i, 0)
            if mat[i][m-1] == 1 and visited[i][m-1] == 0:
                dfs(i, m-1)

        cnt = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and visited[i][j] == 0:
                    cnt += 1
        return cnt