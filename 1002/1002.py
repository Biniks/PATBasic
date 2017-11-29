lst=['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
x=input()
Sum=0
for i in range(len(x)):
    Sum+=int(x[i])
result=[]
while Sum!=0:
    result.append(Sum%10)
    Sum=Sum//10
if len(result)>1:
    for i in range(len(result)-1):
        print(lst[result[-i-1]],end=' ')
print(lst[result[0]])