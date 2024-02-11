# sub.py
# program that reads in two numbers and subtracts the first one from the second one
# author: Nataliia Dragunova

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
sub = num1 - num2
print ("{} minus {} is {}".format(num1, num2, sub));

# Input returns a str, so we need to convert this to an int 
# if we are going to do arithmetic on it 