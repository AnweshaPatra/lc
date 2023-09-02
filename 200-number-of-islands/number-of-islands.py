class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0]*m for _ in range(n)]
        ans = 0

        def bfs(i, j):
            vis[i][j] = 1
            q = []
            q.append([i, j])
            while len(q) != 0:
                node = q.pop(0)
                row = node[0]
                col = node[1]
                print(row, col)
                #traverse neighbors and mark
                for delrow in range(-1, 2):
                    for delcol in range(-1, 2):
                        if delrow == -1 or delrow == 1:
                            delcol = 0
                        nrow = row + delrow
                        ncol = col + delcol
                        if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == "1" and vis[nrow][ncol] == 0:
                            vis[nrow][ncol] = 1
                            q.append([nrow, ncol]) 


        for i in range(n):
            for j in range(m):
                if vis[i][j] == 0 and grid[i][j] == "1":
                    bfs(i, j)
                    ans += 1
        return ans