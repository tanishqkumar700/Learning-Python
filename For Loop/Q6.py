#PRINT THE SUM OF ALL EVEN AND ODD NUMBERS IN A RANGE SEPARATELY.

n = int(input("Enter the number:"))

SumEven = 0
SumOdd = 0

for i in range(1,n+1):
	if(i % 2 == 0):
		SumEven += i
	else:
		SumOdd += i

print(f"Sum of odd numbers is {SumOdd}.")
print(f"Sum of even numbers is {SumEven}.")
