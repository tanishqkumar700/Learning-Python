# A PROGRAM TO COMBINE TWO DICTIONARY BY ADDING VALUES FOR COMMON KEYS.

d1 = {10:100,20:200,40:300}
d2 = {40:400,50:500,60:600}

for i in d2:
	if i in d1.keys():
		d1[i] += d2[i]
	else:
		d1[i] = d2[i]

print(d1)