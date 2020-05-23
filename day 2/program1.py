n = int(input("Enter number: "))
sum = 0
temp = n
while temp > 0:
   digit = temp % 10
   sum = sum + digit ** 3
   temp = temp // 10
if n == sum:
   print("Given number is an Armstrong number")
temp=n
reverse = 0
while(temp>0):
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp//10
    if(reverse==n):
        print("Given number is palindrome number")

temp = n
if temp > 1:
    for i in range(2,temp):
        if(temp%i)==0:
            break
    print("Given number is prime number")

if(n%2==0):
    print("Given number is even number")
else:
    print("Given number is odd number")

