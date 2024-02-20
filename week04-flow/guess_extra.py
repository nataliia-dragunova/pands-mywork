# guess_extra.py
#  get the program to generate a random number between 0 and 100 to guess
# author: Nataliia Dragunova


import random
num1 = int(input("Enter first number of the range:"))
num2 = int(input("Enter second number of the range:"))
number_to_guess = random.randint (num1, num2)
guess = int(input(f"Please guess the number in rage {num1} and {num2}:")) 
while guess != number_to_guess:
    if guess < number_to_guess:     
       print ("too low")
    else:     
       print ("too high")     
    guess = int(input("Please guess again:")) 
print ("Well done! Yes the number was", number_to_guess)