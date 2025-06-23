# WRITE A PYTHON SCRIPT TO MERGE TWO PYTHON DICTIONARIES.
 
d1 = {10:100,20:200,30:300}
d2 = {40:400,50:500,60:600}

d1.update(d2)
print(d1)

for i in d2:
	d1[i] = d2[i]
print(d1)