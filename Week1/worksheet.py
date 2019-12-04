# Question 1: Write a line of code that will print your name
print("Valerie")


# Question 2: How do you enter a comment in a program?
# you write a hashtag #


# Question 3: What do the following lines of code output? ALSO: Why do they give a different answer?
print(2 / 3)
print(2 // 3)  # This one rounds down


# Q4: Write a line of code that creates a variable called pi and sets it to an appropriate value.
pi = 10


# Q5: Why does this code not work?
'''
A = 22
print(a)  #because a was not created as a variable --> A was created (not the same!)
'''


# Q6: All of the variable names below can be used. But which ONE of these is the better variable name to use?
'''
a #This one: lower case letter
A

Area
AREA
area #This one: lower case

area_of_rectangle #This one: lower case
Area_Of_Rectangle
'''


# Q7: Which of these variables names are not allowed in Python?
# (More than one might be wrong. Also, this question is not asking about improper names,
# just names that aren't allowed. Test them if you aren't sure.)
'''
apple 
Apple
APPLE
Apple2
1Apple              #not allowed (no start with number)
account number      #not allowed (no space)
account_number
account.number      #not allowed (no dot)
accountNumber
account#            #not allowed (no #)
pi
PI
fred
Fred
GreatBigVariable
greatBigVariable
great_big_variable
great.big.variable  #not allowed (no dot)
2x                  #not allowed (no start with number)
x2x                
total%              #not allowed (no Sonderzeichen)
#left               #not allowed (no Sonderzeichen)
'''


# Q8: Why does this code not work?
'''
print(a)
a = 45      # The value of the variable was defined after printing 
'''


# Q9: Explain the mistake in this code:
pi2 = float(3.14)
print(pi2)
# Constant should to be written in capital letter (PI2 = 3.13)
# no need for float since it's already a float


# Q10: This program runs, but the code still could be better. Explain what is wrong with the code.
'''
radius = float(input("Radius:"))
x = 3.14  # This two lines are unnecesary
pi3 = x   #
area = pi3 * radius ** 2
print(area)
# Better (no redundant code):
radius = float(input("Radius:"))
pi3 = 3.14
area = pi3 * radius ** 2
print(area)
'''


# Q11: Explain the mistake in the following code:
x = 4
y = 5
# a = ((x) * (y))
a = x * y  # You dont need the brackets
print(a)


# Q12: Explain the mistake in the following code:
x = 4
y = 5
# a = 3(x + y)
a = 3 * (x + y)  # You need to write *
print(a)


# Q13: Explain the mistake in the following code:
# radius = input(float("Enter the radius:"))  #Wrong order of float & input
# radius = float(input("Enter the radius:"))


# Q14: Do all these print the same value? Which one is better to use and why?
print(2/3+4)
print(2 / 3 + 4)
print(   2 /    3+    4  )
# Yes. Due to the style guide the 2. one is the best (spacing).


# Q15: What is a constant?
# A variable (ex. A) which will not be updated. It stays constant without changes later on.


# Q16: How are variable names for constants different than other variable names?
# Variable: a (lower case) / Constant variable: A (upper case)


# Q17: What is a single quote and what is a double quote? Give and label an example of both.
print('Hihi')
print("Hoho")
# When should I use what? --> Doesn't matter


# Q18: Write a Python program that will use escape codes to print a double-quote and a new line using the
# Window's standard. (Note: I'm asking for the Window's standard here. Look it up out of Chapter 1.)
print("\"")
print("Now I will start a \nnew line")


# Q19: Can a Python program print text to the screen using single quotes instead of double quotes?
# Yes
print('Hello')


# Q20: Why does this code not calculate the average?
print(3 + 4 + 5 / 3)
# Normal calculation rules
print((3 + 4 + 5) / 3)


# Q21: What is an ``operator'' in Python?
# + - * /


# Q22: What does the following program print out?
x = 3
x + 1
print(x)
# 3 (since x + 1 is not saved in the variable)


# Q23: Correct the following code:
# user_name = input("Enter your name: )"
# Correct: user_name = input("Enter your name: ")


# Q24: Correct the following code:
# value = int(input(print("Enter your age"))) #You cant print and input at the same time
value = int(input("Enter your age:"))
print(value)