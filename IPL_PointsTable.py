L = [ ]
for line in range(8):
    line = input().split(',')
    L.append(line)
#print(L)

point_table = {}

def winningTeam(L):
    for i in L:
      return L[0]
winningTeam(L)

def restTeams(L):
    for i in L:
      rest = L[1: ]
      return len(rest)
restTeams(L)

def pointsTable(L):
    for i in L:
        win = winningTeam(i)
        rest_team = restTeams(i)
        point_table[win] = rest_team
    return point_table
pointsTable(L)

point_table = (sorted(point_table.items(), key=lambda k:k[1], reverse=True))
#print(point_table)

for key,value in point_table:
    print (str(key)+':'+str(value))