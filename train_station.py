num_trains=int(input())
station_dict={}
for i in range (num_trains):
    
    name_train=input()
    num_compart=int(input())
    
    my_dict={}      
    for j in range(num_compart):
        key,value=input().split(',')
        my_dict[key]=int(value)
          
    station_dict[name_train]=my_dict