d = {}
def freq_to_words(words):
    s = set(words)
    for i in s:
        count = words.count(i)
        d[i] = count
        d.update(d)

    flipped = {}
    
    for key, value in d.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    #return str(flipped)

    for key, value in flipped.items():
        value = ','.join(value)
        flipped[key] = value

    for key in sorted (flipped.keys()) :
        print (key,':', flipped[key])
              

lst = ['two', 'to', 'two', 'to', 'two', 'two']
lst1 = ['a', 'random', 'collection', 'a', 'another', 'a', 'random']
print(freq_to_words(lst1))