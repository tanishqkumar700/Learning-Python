#CHECK IF LIST IS SORTED OR NOT.

l = [1,2,3,4,5]



# sort = None
# for i in range(len(l)-1) :  # (4)
# 	if l[i] < l[i+1] :
# 		sort = True
# 	else:
# 		sort = False

# if sort:
# 	print("List is sorted.")
# else :
# 	print("List is not sorted.")


# OR

for i in range(len(l)-1) :  # (4)
	if l[i] < l[i+1] :
		continue
	else:
		print("List is not sorted.")
		break
else :
	print("List is sorted.")