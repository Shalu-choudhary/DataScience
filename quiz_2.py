# COUNT THE NO. OF INT,FLOAT,STRING AND BOOL FROM THE LIST

ls=[23,32,44,55,5.5,6.7,1.2,"shalu","upflairs",True,False]

count_bool=0
for i in ls:
    if(i==True or i==False):
        count_bool+=1
print("The no. of boolean type is :",count_bool)

count_int=0
for i in ls:
    if type(0)==type(i):
        count_int+=1
print("the no. of int is :",count_int)

count_float=0
for i in ls:
    if type(0.0)==type(i):
        count_float+=1
print("the no. of float is :",count_float)

count_string=0
for i in ls:
    if type("")==type(i):
        count_string+=1
print("the no. of string is :",count_string)
