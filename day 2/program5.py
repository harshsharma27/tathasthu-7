nu = input("Enter the number: ")
n= int(nu)
a =n
p="*"
for i in range(0,n):
    for j in range(i,n-1):
        print(str(a)+p,end="")
        # print("*", end="")
    print(a)
    a=a-1

a=1
for i in range(0,n):
    for j in range(0,i):
        print(a,end="")
        print("*", end="")
    print(a)
    # print("\n")
    a=a+1
