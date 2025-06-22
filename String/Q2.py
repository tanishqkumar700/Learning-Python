#CHECK STRING IS PALINDROME OR NOT

A = "MADAm"
B = ""
for i in range(len(A)-1,-1,-1):
	B = B + A[i]

if(A.lower() == B.lower()):
	print(f"{A} is palindrome.")
else:
	print(f"{A} is not palindrome.")