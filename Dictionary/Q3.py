#COUNT THE FREQUENCY OF EACH ELEMENT OF A  LIST.

A = [1,1,1,2,2,3,3,3,3,3,4,4,5,5,6,6,7,8,6,9,9,0,0,0,0]

d = {}
for i in A:
	if i in d.keys():
		d[i] += 1
	else:
		d[i] = 1
print(d)