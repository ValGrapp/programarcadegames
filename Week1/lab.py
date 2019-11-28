# Part A
# Create a program that asks the user for a temperature in Fahrenheit,
# and then prints the temperature in Celsius. Search the Internet for the
# correct calculation. Look at Chapter 1 for the miles-per-gallon example to get an idea of what should be done.

temp_fahrenheit = float(input("Insert temp in fahrenheit: "))
temp_celsius = (temp_fahrenheit - 32) / 1.8
print("Temp in Celsius:", temp_celsius)
# correct


# Part B
# Create a new program that will ask the user for the information needed
# to find the area of a trapezoid, and then print the area.
# The formula for the area of a trapezoid is: A = 0.5 * (x1*x2) * h

print("Area of a trapezoid")
height = float(input("Enter the height of the trapezoid: "))
lenght_bottom = float(input("Enter the length of the bottom base: "))
lenght_top = float(input("Enter the length of the top base: "))
area = 0.5 * (lenght_bottom + lenght_top) * height
print("The area is: ", area)
# correct


# Part C
# Create your own original problem and have the user plug in the variables.
# If you are not in the mood for anything original, choose an equation from this list:
print("Area of a cirlce")
pi = 3.14
radius = float(input("Enter the radius of the circle: "))
area = pi * (radius ** 2)
print("The area is: ", area)
