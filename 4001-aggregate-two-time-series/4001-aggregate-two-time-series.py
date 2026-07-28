class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        
        res=[]

        s1_ind=0
        s2_ind=0
        while s1_ind<len(series1) and s2_ind<len(series2):
           
            res.append([min(series1[s1_ind][0],series2[s2_ind][0]),series1[s1_ind][1]+series2[s2_ind][1]])

            if series1[s1_ind][0]<series2[s2_ind][0]:
                s1_ind+=1
            elif series1[s1_ind][0]>series2[s2_ind][0]:
                s2_ind+=1
            else:
                s1_ind+=1
                s2_ind+=1
            
            
        while s1_ind<len(series1):
            res.append(series1[s1_ind])
            s1_ind+=1
        
        while s2_ind<len(series2):
            res.append(series2[s2_ind])
            s2_ind+=1
        print(res)
        return res
            
        

            
        
        

