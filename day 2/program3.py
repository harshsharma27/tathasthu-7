n = int(input ("Enter the number: ")) 
for i in range(1,n+1):
	print( " "*i+"*"+"  "*(n-i)+"*")
for i in range(1,n+1):
	print(" "*(n-i+1)+"*"+" "*(2*i-2)+"*")
