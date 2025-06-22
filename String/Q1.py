#Reverse a string without using in built functions.

A = "Tanishq Kumar"
ReverseA = A[::-1]
print(ReverseA)

#or 
B=""
length  = len(A)
for i in range(len(A)-1,-1,-1):
	B = B + A[i]

print(B)