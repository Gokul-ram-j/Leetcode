class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row=len(mat)
        col=len(mat[0])

        rowList=[0 for i in range(row)]
        colList=[0 for i in range(col)]
        for i in range(row):
            for j in range(col):
                if mat[i][j]==1:
                    rowList[i]+=1
                    colList[j]+=1
        res=0
        for i in range(row):
            for j in range(col):
                if mat[i][j]==1 and rowList[i] ==1 and colList[j]==1: res+=1
        
        return res