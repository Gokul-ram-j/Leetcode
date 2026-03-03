class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh_orange=0
        queue=[]
        min_passed=0
        row=len(grid)
        col=len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append([i,j])
                elif grid[i][j]==1:
                    fresh_orange+=1
        
        while(queue and fresh_orange>0):
            new_queue=[]
            direc=[(-1,0),(1,0),(0,-1),(0,1)]
            min_passed+=1
            for nr,nc in queue:
                for dr,dc in direc:
                    drow=nr+dr
                    dcol=nc+dc
                    if 0<=dcol<col and 0<=drow<row and grid[drow][dcol]==1:
                        new_queue.append([drow,dcol])
                        fresh_orange-=1
                        grid[drow][dcol]=2

            queue=new_queue
        if fresh_orange==0:
            return min_passed
        
        return -1
                    
       


        