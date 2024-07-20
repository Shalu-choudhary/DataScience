
ls=[65,43,23,21,12,55,46,77,87]
def max_no(ls):
     max_no=0
     for i in ls:
         if i>max_no:
          max_no=i
     return max_no


def min_no(ls):
     min_no=ls[0] 
     for i in ls:
         if i<min_no:
          min_no=i
     return min_no

ls=[65,43,23,21,12,55,46,77,87]
def sort_fun(ls):
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if ls[i]>ls[j]:
                ls[i],ls[j]=ls[j],ls[i]
    return ls