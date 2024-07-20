#map


# ls=[3,2,4,5,34]
# output=list(map(lembda x:x**2,ls))
# print(output)
# def fun(item):
#     return item**2

# ls = []
# for item in ls:
#     square=fun(item)
#     ls.append(square)

# EXCEPTION------>>
# 1) COMPILE TIME   2) RUN TIME
# there are 4 block:= try,except,else,finally
# try-> if there are error in try then it throw the code into the except
# try:
#     name=input("enter your name")
#     age=int(input("enter your age"))
#     print("i am ",name,"i am ",age,"year old")
# except:
#     print("error is occured but dont worry we will execute your remaining line")
    
# else:
#     print("error is not occure")

# finally:
#     print("i will be always")
  
# a=int(input("hiii enter something"))
# try:  
#     num1=int(input("enter first number: "))
#     num2=int(input("enter second number : "))
#     result=num1/num2   
#     print(result)
# except ZeroDivisionError:
#     print(" zerodivisionerror error is occured! plz dont insert zero at the second place")
# except ValueError:
#     print(" two type of error string error which is value error ! plz enter only intezer value")
# print("i am important")

# print("hello world') #syntex error -- not well defined then it is execute

ls=[52,41,63,96,85,96,44,55,56,65]
# target=int(96
# input("enter your target item : "))
# position=int(input("enter a position : "))

# return target item 
# return position

# try:
#     target=int(input("enter your target item : "))
#     position=int(input("enter a position : "))
#     for i in range(len(ls)):
#         if ls[i]==target:
#            print(" target is founded at index",i)
#            print("at index the item is ",ls[position])
#            break
       
# except ValueError:
#     print("plz enter intezer value")
# except  IndexError:
#     print("plz enter correct index")
# except TypeError:
#     print("plz enter correct type ")
    
try:
    age=int(input("enter your age"))
except Exception as e:
    print(e)
    
# .ipynb-----> interactive python notebook jupyter notebook
    












    
    
    



