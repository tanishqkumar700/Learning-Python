#PRINT POSITIVE AND NEGATIVE ELEMENTS OF A LIST.

l = [34,53,-97,78,-57,46,-4,-69-5,78,-87]

neg = []
pos = []
for i in l:
	if i<0:
		neg.append(i)
	else:
		pos.append(i)

print(f"negative numbers are {neg}")
print(f"positive numbers are {pos}")