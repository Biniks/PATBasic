def cut(n):
    if n % 2 == 1:
        return (n*3+1)/2
    return n/2


if __name__ == '__main__':
    n = int(input())
    count = 0
    while n != 1:
        n = cut(n)
        count += 1
    print(count)
