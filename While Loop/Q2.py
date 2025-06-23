# ACCEPT A NUMBER AND PRINT ITS REVERSE.

A = int(input("Enter the number: "))
rev = 0
while(A>0):
	rev = rev *10 + A % 10
	A = A // 10
print(rev)	
print(A)