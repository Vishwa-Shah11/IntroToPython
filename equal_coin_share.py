coins = int(input())
f1 = int(input())
f2 = int(input())
f3 = int(input())

output = 'UNFAIR'

if (f1+f2+f3 == coins):
    if (f1 > 0 and f2 > 0 and f3 > 0):
        if (f1 != f2 and f2 != f3 and f3 != f1):
            output = 'FAIR'

print(output)