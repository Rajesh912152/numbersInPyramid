n=int(input())
s=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print(s+j,end=" ")
    print()