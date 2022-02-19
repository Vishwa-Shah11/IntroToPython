start = input()
end = input()
bishop_move = 'NO'

#print(ord(end[0]))
#print(int(end[1]) - int(start[1]))
dx = abs(ord(end[0]) - ord(start[0]))
print(dx)
dy = abs(int(end[1]) - int(start[1]))
print(dy)
if (dx == dy) and (dx > 0):
    bishop_move = 'YES'
 
print(bishop_move)
