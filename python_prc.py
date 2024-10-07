# x=[1,2,3,4,5]
# y=[1,2,6,7]
# c=x+y
# print(c)
# lis=[21,22,23,24,25]

# for i in range(1,3):

#   print(i)

#   for j in range(1,6):

#     print(j,end="")

#   print()

# list1=[1,0,1,0,0,1]

# list2=[23,45,78,99,88,32]

# j=0

# for i in range(len(list1)):

#   if(list1[i]==1):

#     num=list2[j]


#     sum=0

#     rem=0

#     while(num>0):

#       rem=num%10

#       sum=sum*10+rem

#       num=num//10

#     list2[i]=sum

#   j=j+1

# print(list2)

# name=list("GuviGeek")

# i=0;

# temp=''

# name1=''

# m=(len(name)//2)-1

# for j in range(len(name)-1,m,-1):

#     if(i<j):

#         temp=name[i]

#         name[i]=name[j]

#         name[j]=temp

#     i+=1

# name1="".join(name)

# print(name1[::-1])

# list1=[2,4,6]

# for i in range(0,1):

#   for j in range (len(list1)):

#     list1[j]=list1[i]//list1[j]

#     if(j==1):

#       print(list1)

# list1=[100,200,300,400,500,600]

# for i in range(0,len(list1),2):

#     print(i,end="")
    
# t = (1, 2, 4, 3),

# print (t[1 : -1] ) 

# print("Good " + 1 + 2 + 3)

# a=input("Enter a number:")

# b=a*a

# print("The square of number is:",b)

# arr = [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

# for i in range(0, 4):

#     print(arr[i].pop())
income=4001
if income > 3000:
    print("Income is greater than 3000")
elif income > 4000:
    print("Income is greater than 4000")
    
a="10"

b="20"

c=a+b

print(c)

print([i.lower() for i in "HELLO"])

list1=[1,2,3,4,5,6]

a=int(input("Enter a number:"))

if a not in list1:

    list1.append(a)

print(list1)