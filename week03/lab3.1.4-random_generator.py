# random_generator.py
# program that prints out a random number between 1 and 10 
# author: Nataliia Dragunova
'''
import random # module
number = random.randint (1,10)
print ("here is a random number {}".format(number));
'''
import random # module
num1 = int(input("Enter first number of the range:"))
num2 = int(input("Enter second number of the range:"))
number = random.randint (num1,num2)
print ("here is a random number {}".format(number));                       