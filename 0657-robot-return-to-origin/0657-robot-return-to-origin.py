class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        lr=0
        ud=0
        for move in moves:
            if   move  =="L" :lr+=1
            elif move  =="R" :lr-=1
            elif move  =="U" :ud+=1
            elif move  =="D" :ud-=1
        
        return lr==0 and ud==0
        
