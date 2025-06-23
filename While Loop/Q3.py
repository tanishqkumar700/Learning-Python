# ACCEPT A NUMBER AND CHECK IF IT IS A PALINDROMIC NUMBER.

A = int(input("Enter the number: "))
temp = A
rev = 0
while(temp>0):
	rev = rev *10 + temp % 10
	temp = temp // 10

if(A == rev):
	print(f"{A} is a palindromic number")
else:
	print( f"{A} is not a palindromic number")