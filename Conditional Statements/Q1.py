#EXCEPT TWO NUMBERS AND PRINT THE GREATEST NUMBER

def greatest_of_two_numbers(num1, num2):
    """This function takes two numbers as input and returns the greatest of the two."""
    if num1 > num2 : 
        return num1
    elif num1 < num2:
        return num2
    else:
        return "Both are same"
    

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

ans = greatest_of_two_numbers(a,b)
print(f"The largest number among {a} and {b} is {ans}")
