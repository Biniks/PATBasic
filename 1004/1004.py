def display(lst):
    print(lst[0],end=' ')
    print(lst[1])
    return

from operator import itemgetter
n=int(input())
lst=[]
for i in range(n):
    lst.append(input())
    lst[-1]=lst[-1].split(' ')
    lst[-1][-1]=int(lst[-1][-1])
sort_list=sorted(lst,key=itemgetter(2))
display(sort_list[-1])
display(sort_list[0])