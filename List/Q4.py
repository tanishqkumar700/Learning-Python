#FIND THE SECOND LARGEST NUMBER.

l = [12,16,13,19,17]#[56,92,452,985,125,265,756,125]

largest =l[0]
index = 0
sec_largest = l[0]
sec_larg_index = 0
for i in range(len(l)):
	if (l[i]>largest):
		sec_largest = largest
		sec_larg_index = index

		largest = l[i]
		index = i

	# when value is smaller than largest but greater than secondllargest  i.e. largest = 19, next is 17 that is smaller than largest but greater than 16 i.e. current second largest.	
	elif (l[i] > sec_largest):
		sec_largest = l[i]
		sec_larg_index = i

print(f" Second Largest number in this list is {sec_largest} at index {sec_larg_index}.")