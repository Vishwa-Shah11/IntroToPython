n = input().split(',')
lsum = 0
rsum = 0
for i in n:
    mid = (len(n)+1) // 2
    left = (n[:mid])
    right = (n[mid:])
for l in left:
    a = int(l)
    lsum += a
for r in right:
    b = int(r)
    rsum += b

if (lsum>rsum):
    print('left-heavy')
if (rsum>lsum):
    print('right-heavy')
if (lsum == rsum):
    print('balanced')

'''
print(mid)
print(left)
print(lsum)
print(right)
print(rsum)
'''