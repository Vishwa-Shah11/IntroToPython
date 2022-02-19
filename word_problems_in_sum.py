n = input().split()
#print(n)
#s = set(n)
#print(s)
l = []
s=[]
for i in n:
    if (i == 'plus'):
        sign = i.replace('plus', '+')
        l.append(sign)
    if (i == 'minus'):
        sign = i.replace('minus', '-')
        l.append(sign)
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
#print(l)   


if len(l) % 2 ==0:
    heet=[]
    for i in range(0,len(l)-1,2):
        string= l[i]+l[i+1]
        heet.append(string)


if len(l) % 2 !=0:
    heet=[l[0]]
    #print(heet)
    for i in range(1,len(l)-1,2):
        string= l[i]+l[i+1]
        heet.append(string)
        
#print(heet)   

vishwa=list(map(int,heet))
#print(vishwa)

sum=0
for i in range (len(vishwa)):
    sum=sum+vishwa[i]
print(sum)