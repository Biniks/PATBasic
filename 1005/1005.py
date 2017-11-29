def cut(n):
    if n==1:
        return
    if n%2==1:
        return (3*n+1)/2
    return n/2

def display(lst):
    for i in range(len(lst)-1):
        print(lst[i],end=' ')
    print(lst[-1])

if __name__=="__main__":
    n=int(input())
    num_list=input().split(' ')
    num_list=list(map(int,num_list))
    num_temp=[]
    for item in num_list:
        num_temp.append(item)
    for i in range(len(num_list)):
        temp=num_list[i]
        if temp not in num_temp:
            continue
        while temp!=1:
            temp=cut(temp)
            if temp in num_temp:
                num_temp.remove(temp)
    num_temp=sorted(num_temp,reverse=True)
    display(num_temp)