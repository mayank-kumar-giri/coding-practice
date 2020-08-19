import queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = [[False for i in range(columns)] for j in range(rows)]
        q = queue.Queue()
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    q.put([i,j,0])
                    visited[i][j] = True
                    
        maximum_time_taken = 0
        neighbours = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        while not q.empty():
            curr_x, curr_y, curr_depth = q.get()
            
            if maximum_time_taken < curr_depth:
                maximum_time_taken = curr_depth
            
            for neighbour in neighbours:
                increment_x, increment_y = neighbour
                
                new_x = curr_x + increment_x
                new_y = curr_y + increment_y
                new_depth = curr_depth + 1
                
                if (new_x >= 0 and new_x <= (rows-1)) and (new_y >= 0 and new_y <= (columns-1)):
                    if (not visited[new_x][new_y]) and (grid[new_x][new_y]==1):
                        q.put([new_x, new_y, new_depth])
                        visited[new_x][new_y] = True
        
        done = False
        for i in range(rows):
            for j in range(columns):
                if (visited[i][j] == False) and (grid[i][j] == 1):
                    maximum_time_taken = -1
                    done = True
                    break
            if done:
                break
                    
        
        return maximum_time_taken
