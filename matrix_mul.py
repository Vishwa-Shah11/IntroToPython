import numpy

n = int(input())
#mat = np.zeros((n,n))
a = []
b = []

for i in range(n):
  #mat[i] = input().split(',')
  a.append(list(map(int, input().rstrip().split(',')))) 
#print(a)
for i in range(n):
  b.append(list(map(int, input().rstrip().split(','))))
#print(b)

x = numpy.mat(a)
y = numpy.mat(b)
mul = x*y
print(mul)