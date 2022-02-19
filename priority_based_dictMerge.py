D1 = {1: 2, 2: 3, 3: 4}
D2 = {1: 10, 4: 15, 5:10}
D = {}

def merge(D1, D2, priority):
    if (priority == 'first'):
        D.update(D2)
        D.update(D1)
    elif (priority == 'second'):
        D.update(D1)
        D.update(D2)
    return D #merged dictionary
print(merge(D1, D2, 'first'))