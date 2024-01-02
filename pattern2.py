
n =int(input())
for i in range(0,n):
    for j in range(i,-1,-1):
        b = ord("A")
        a = chr(b+n-1-j)
        print(a,end="")
    b+=1
    print()


