n = int(input())
L = [ ]
for i in range(n):
    line = input().split(',')
    L.append(line)
#print(L)

def first(L):
    return L[0]
first(L)

def rest(L):
    return L[1: ]
rest(L)

def prereq(L):
    D = dict()
    for clist in L:
        main = first(clist)
        pre_main = rest(clist)
        D[main] = pre_main
    return D
print(prereq(L))

'''
#Verified
def get_basic(D):
    basic = [ ]
    for main in D:
        for course in D[main]:
            if course not in D:
                basic.append(course)
    return set(basic)
'''
'''
#Verified
def get_basic(D):
    all_courses = set()
    for main in D:
        all_courses.add(main)
        for course in D[main]:
            all_courses.add(course)

    basic = set()
    for course in all_courses:
        if course not in D:
            basic.add(course)
    return basic
'''
def get_basic(D):
    all_courses = set()
    for main in D:
        all_courses.add(main)
        for course in D[main]:
            all_courses.add(course)
            
    prereq_courses = set()
    for main in D:
        prereq_courses.add(main)
      
    basic = all_courses - prereq_courses
    return basic
print(get_basic(prereq(L)))

'''
#Verified
def pinnacle(D):
    S = set()
    for main_1 in D:
        flag = True
        for main_2 in D:
            if main_1 == main_2:
                continue
            if main_1 in D[main_2]:
                flag = False
                break
        if flag:
            S.add(main_1)
    return S
'''

#Verified
def pinnacle(D):
    S = set()
    for main_1 in D:
        flag = True
        for main_2 in D:
            if main_1 in D[main_2]:
                flag = False
                break
        if flag:
            S.add(main_1)
    return S
print(pinnacle(prereq(L)))

def get_deep(D):
    deep = [ ]
    maxpre = 1
    for main in D:
        if len(D[main]) > maxpre:
            maxpre = len(D[main])
            deep = [main]
        elif len(D[main]) == maxpre:
            deep.append(main)
    return deep
print(get_deep(prereq(L)))