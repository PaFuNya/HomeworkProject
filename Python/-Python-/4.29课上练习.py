#两个乒乓球队进行比赛，各出3人，甲为a,b,c，乙为x,y,z，已知a不和x比，c不和x,z比，编写出队员的名单
team1=['a','b','c']
team2=['x','y','z']
for i in team1:
    for j in team2:
        if(i=='a' and j=='x'):
            continue
        if(i=="c" and (j=="x" or j=="z")):
            continue
        print(i,j)
