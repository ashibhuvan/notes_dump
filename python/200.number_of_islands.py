class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i: int, j: int, visited: List[List[int]]):
            visited[i][j] = 1
            
            #Up
            if i != 0 and grid[i - 1][j] == "1" and visited[i - 1][j] == 0:
                dfs(i - 1, j, visited)
            #Down
            if i != len(grid) - 1 and grid[i + 1][j] == "1" and visited[i + 1][j] == 0:
                dfs(i + 1, j, visited)
            #Left
            if j != 0 and grid[i][j - 1] == "1" and visited[i][j - 1] == 0:
                dfs(i, j - 1, visited)
            #Right
            if j != len(grid[0]) - 1 and grid[i][j + 1] != "0" and visited[i][j + 1] == 0:
                dfs(i, j + 1, visited)
            return
        
        islands = 0
        visited = [[0 for _ in row] for row in grid]
        
        for i,row in enumerate(grid):
            for j,elem in enumerate(row):
                if elem == "0":
                    continue
                if elem == "1" and visited[i][j] == 0:
                    # Increase number of island
                    # Mark as visited
                    dfs(i, j, visited)
                    islands += 1 
        return islands
