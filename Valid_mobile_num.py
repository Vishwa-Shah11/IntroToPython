phone_num = input()
flag = False

if (len(phone_num) == 10):
  if ((phone_num[0] == '6') or (phone_num[0] == '7') or (phone_num[0] == '8') or (phone_num[0] == '9')):
    for i in phone_num:
      count = phone_num.count(i)
    if (count <= 7):
      flag = True
    else:
      flag = False
  else:
    flag = False   
else:
  flag = False

flag_new = False
val = 0
for i in range(5):
    if (val<=5):
        counter = 1
        for j in range(i+1, i+6):
          if (phone_num[i] != phone_num[j]):
              break
          else:
              counter += 1
              val = counter  
          #print(val) 
if (counter<=5):
  flag_new = True
else:
  flag_new = False

if flag == True and flag_new == True:
  print('valid')
else:
  print('invalid')