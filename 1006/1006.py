n=eval(input())
result=[]
for i in range(3):
    result.append(n%10)
    n=n//10
print('B'*result[-1]+'S'*result[-2],end='')
for i in range(result[0]):
    print(i+1,end='')