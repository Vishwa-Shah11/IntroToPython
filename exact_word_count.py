def exact_count(para, n):
  
    result = False
    count = 0
    l = para.split()
    print(l)
    s = set(l)
    print(s)
    for word in s:
        count = l.count(word)
        if count == n:
            print(count)
            result = True
        else: 
            result = False

    return result

p = 'good word many good works good real choice'
p1 = 'this is a sentence there are many sentences is working fine is good to go is'
print(exact_count(p, 3))