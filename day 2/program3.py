n = int(input("Enter the number: "))
k=n
h = n//2

for i in range(0,h):
    for m in range(0,i):
        print(" ",end="")

    print("*",end="")
    for j in range(i+1,k):
        if(j==k-1):
            print("*",end="")
        else:
            print(" ",end="")
    k = k-1
    print("\n")
k=h
for i in range(h,n):
    for m in range(i+1,n):
        print(" ",end="")

    print("*",end="")
    for j in range():
        if(j==k-h):
            print("*",end="")
        else:
            print(" ",end="")
    k = k+2
    print("\n")