n = input().split()

l = []
l1 = []
for i in n:
    if (i == 'plus'):
        dig = i.replace('plus', '11')
        l.append(dig)
    if (i == 'minus'):
        dig = i.replace('minus', '12')
        l.append(dig)
    if (i == 'zero'):
        dig = i.replace('zero', '0')
        l.append(dig)
    if (i == 'one'):
        dig = i.replace('one', '1')
        l.append(dig)
    if (i == 'two'):
        dig = i.replace('two', '2')
        l.append(dig)
    if (i == 'three'):
        dig = i.replace('three', '3')
        l.append(dig)
    if (i == 'four'):
        dig = i.replace('four', '4')
        l.append(dig)
    if (i == 'five'):
        dig = i.replace('five', '5')
        l.append(dig)
    if (i == 'six'):
        dig = i.replace('six', '6')
        l.append(dig)
    if (i == 'seven'):
        dig = i.replace('seven', '7')
        l.append(dig)
    if (i == 'eight'):
        dig = i.replace('eight', '8')
        l.append(dig)
    if (i == 'nine'):
        dig = i.replace('nine', '9')
        l.append(dig)

for i in l:
    dig = int(i)
    l1.append(dig)
  
b = []
c=[]

if(l1[0]!=12 and l1[0]!=11):
    for i in range(len(l1)-1):
        if (l1[i] == 12):
            heet = -abs(l1[i+1])
            b.append(heet)
        if (l1[i] == 11):
            heet = l1[i+1]
            #print(abs, 'abs')
            c.append(heet)   
    final=c+b+[l1[0]]  
    #print(final)
else:
    for i in range(len(l1)-1):
        if (l1[i] == 12):
            heet = -abs(l1[i+1])
            b.append(heet)
        if (l1[i] == 11):
            heet = l1[i+1]
            #print(abs, 'abs')
            c.append(heet)   
    final=c+b      

sum = sum(final)
print(sum)