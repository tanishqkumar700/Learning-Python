# MEAN OF LIST ELEMENTS

l = [1,2,3,4,5]
sum = 0
for i in l:
	sum = sum + i

mean = sum/len(l)

print(f"Mean of list elements is: {mean}")