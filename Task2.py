import math

number = float(input("Enter a number: "))

if number <= 0:
    print("Square root and logarithm are not defined for zero or negative numbers.")
else:

    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)

    print("Square root:", square_root)
    print("Natural logarithm:", natural_log)
    print("Sine of the number:", sine_value)

