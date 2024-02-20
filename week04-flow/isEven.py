# isEven.py
# to check if a number is odd or even
# author: Nataliia Dragunova

num = int(input("Enter some number:"))
if num % 2 == 0:
   print ("number is even")
else:
   print ("number is odd")

'''
# version - thoughts about zero
num = int(input("Enter some number:"))
if num == 0 or num % 2 == 0:
    print (f"{num} is even number")
else:
   print (f"{num} is odd number")

# Andrew's code
number = int(input("enter an integer:"))
if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
'''
  