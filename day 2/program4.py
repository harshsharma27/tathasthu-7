n = int(input("Enter the number: "))
k=n

h = n//2

for i in range(0,h):
    for j in range(i,h):
        print("*",end="")

    print(" ",end="")
    for m in range(0,2*i):

        print(" ",end="")
    for j in range(i,h-1):
        print("*",end="")
    print("*")
    # Reverse pattern
for i in range(0,h):
    for j in range(0,i+1):
        print("*",end="")

    print(" ",end="")
    for m in range(0,k-2):

        print(" ",end="")
    k = k-2
    for j in range(0,i):
        print("*",end="")
    print("*")