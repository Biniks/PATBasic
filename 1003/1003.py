def isRight(lst):
    for char in lst:
        if char not in ['A','P','T']:
            return  False
    if lst.count('P')!=1 or lst.count('T')!=1:
        return False
    indexP=lst.find('P')
    indexT=lst.find('T')
    midNum=indexT-indexP-1
    heaNum=indexP
    finNum=len(lst)-indexT-1
    if midNum<1:
        return False
    if midNum*heaNum!=finNum:
        return False
    return True

if __name__=="__main__":
    n=int(input())
    input_list=[]
    for i in range(n):
        input_list.append(input())
    for item in input_list:
        if isRight(item):
            print('YES')
        else:
            print('NO')