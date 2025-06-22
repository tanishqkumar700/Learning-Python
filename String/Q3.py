#COUNT ALL DIGITS, LETTERS, AND SPECIAL SYMBOLS FROM A GIVEN STRING.

str = "ERGB%#$434yhBVEtfyt5655er34yhnb$%^%$^E%$@#RY"

letters = 0
digits = 0
symbols = 0
for i in str:
	if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
		letters += 1
	elif (ord(i)>=48 and ord(i)<57):
		digits += 1
	else:
		symbols += 1

print(f"No of letters are {letters}")
print(f"No of digits are {digits}")
print(f"No of symbols are {symbols}")


#or

letters = 0
digits = 0
symbols = 0
for i in str:
	if i.isalpha():
		letters += 1
	elif i.isdigit():
		digits += 1
	else:
		symbols +=1

print(f"No of letters are {letters}")
print(f"No of digits are {digits}")
print(f"No of symbols are {symbols}")



print(dir(str))
 