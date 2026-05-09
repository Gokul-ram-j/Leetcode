class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m=len(grid)
        n=len(grid[0])

        layers=min(m,n)//2

        
        for layer in range(layers):
            arr=[]
            left=layer
            right=n-layer-1
            top=layer
            bottom=m-layer-1

            # getting element

            # left->right
            for i in range(left,right+1):
                arr.append(grid[top][i])
            
            # top -> bottom
            for i in range(top+1,bottom):
                arr.append(grid[i][right])
            # right-> left
            for i in range(right,left-1,-1):
                arr.append(grid[bottom][i])
            # bottom -> top
            for i in range(bottom-1,top,-1):
                arr.append(grid[i][left])
            

            # rotating
            
            rot=k%len(arr)
            arr=arr[rot:]+arr[:rot]

            # putting element back
            ind=0
            # left->right
            for i in range(left,right+1):
                grid[top][i]=arr[ind]
                ind+=1

            # top -> bottom
            for i in range(top+1,bottom):
                grid[i][right]=arr[ind]
                ind+=1

            # right-> left
            for i in range(right,left-1,-1):
                grid[bottom][i]=arr[ind]
                ind+=1
            
            # bottom -> top
            for i in range(bottom-1,top,-1):
                grid[i][left]=arr[ind]
                ind+=1
        return grid
                
