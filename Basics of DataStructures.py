import random

nums = []
for i in range(10000):
  nums.append(random.randint(1, 10))
#print(nums)

P = { }
for num in range(1, 11):
    P[num] = 0
for num in nums:
    P[num] += 1
#print(P)

def check(P, N):
    S = 0
    for num in P:
        S += P[num]
    return S == N

#print(check(P, len(nums)))

def most_freq(P):
    freq_num, freq = 1, P[1]
    for num in range(1, 11):
        if P[num] >= freq:
            freq_num = num
            freq = P[num]
    return freq_num
#print(most_freq(P))

#numss = [10, 5, 5, 5, 5, 5, 1, 6, 5, 7, 8, 9]
def streak(nums):
    if 5 not in nums:
        return False 
    count = 0
    for num in nums:
        if num == 5:
            count += 1
            if count == 5:
                return True
        else:
            count = 0
    return False
print(streak(nums))