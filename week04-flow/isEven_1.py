# isEven.py
# to check if a number is odd or even
# author: Nataliia Dragunova

#  keeps prompting the user for a number until the user enters -1
num = int(input("Enter some number:"))
while num != -1:
   if num % 2 == 0:
      print ("number is even")
   else:
      print ("number is odd")
   num = int(input("Enter some number:"))