# div.py
# program that reads in two numbers and 
# divides the first one by the second and give the integer result and the remainder
# author: Nataliia Dragunova
'''
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
div = num1 // num2
rem = num1 - (num2 * div) # % gives the remainder
print ("{} divided by {} is {} with remainder {}".format(num1, num2, div, rem ));
'''
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
div = num1 // num2
rem = num1 % num2 # % gives the remainder
print ("{} divided by {} is {} with remainder {}".format(num1, num2, div, rem ));