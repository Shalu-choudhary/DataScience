#find max or min value from the list without using max() or min() function

ls=[65,43,23,21,12,55,66,77,87]
max=0
for i in ls:
    if i>max:
        max=i
print(max)

min=ls[0]
for i in ls:
    if i<min:
        min=i
print(min)
