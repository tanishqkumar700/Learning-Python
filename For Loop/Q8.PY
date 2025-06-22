#ACCEPT A NUMBER AND CHECK IF IT IS A PERFECT NUMBER OR NOT.
#A NUMBER WHOSE SUM OF FACTORS IS EQUAL TO THE NUMBER ITSELF.
#eg. = 6 -> 1,2,3 = 6 itself note not add 6 as 6 is 

n = int(input("Enter the number: "))
sum = 0

for i in range(1,n):
	if(n%i == 0):
		sum += i

if(sum == n):
	print(f"{n} is a perfect number.")

else:
	print(f"{n} is not a perfect number.")