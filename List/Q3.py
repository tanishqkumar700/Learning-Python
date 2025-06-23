#FIND THE GREATEST ELEMENT AND PRINT ITS INDEX TOO.

l = [456,952,452,985,125,265,756,125]

index = 0 
max = l[index] 

for i in range(len(l)):
	if l[i] > max :
		max = l[i]
		index = i

print(f" Maximum number in this list is {max} at index {index}.")

