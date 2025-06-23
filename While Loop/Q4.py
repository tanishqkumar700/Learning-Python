# Create a Random number guessing game.

import random 

num = random.randint(0,9)
tries = 0
while True:
	guess = int(input("Guess the number:"))

	if(num == guess):
		tries += 1
		print("Correct")
		break
	else:
		tries += 1
		print("Try Again")

print(f"Total number of tries are {tries}")