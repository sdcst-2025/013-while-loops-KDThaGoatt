#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
number = ("")
evenInteger = False

while not evenInteger:
    number = float(input("Enter a number"))
    if number % 1 != 0 or number % 2 != 0:
        print("That is not an even integer")
    else:
        evenInteger = True

print("That is an even integer")