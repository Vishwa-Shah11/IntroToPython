n = input()
count = 0
l = []
correct_num = ''
if (n.isdigit()):
    print('No mistakes')
else:
    for i in n:
        if (i.isalpha()):
            count += 1
            if (i == 'l'):
                i = i.replace('l', '1')
            if (i == 'o'):
                i = i.replace('o', '0')
        l.append(i)
        correct_num = ''.join(l) 

    print(count, 'mistakes')
    print(correct_num)