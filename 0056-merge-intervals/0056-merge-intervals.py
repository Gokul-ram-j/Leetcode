class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        minEnd=intervals[0][0]
        maxEnd=intervals[0][1]
        res=[]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=maxEnd and intervals[i][1]>=maxEnd:
                maxEnd=intervals[i][1]
            elif intervals[i][0]>maxEnd:
                res.append([minEnd,maxEnd])
                minEnd=intervals[i][0]
                maxEnd=intervals[i][1]
        res.append([minEnd,maxEnd])
        return res


            
        