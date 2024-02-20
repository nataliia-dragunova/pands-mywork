# guess2.py
# that prompts the user to guess a number, 
# program tells the user if there guess is too high or too low, each time they guess.
# author: Nataliia Dragunova

number_to_guess = 33  
guess = int(input("Please guess the number:")) 
while guess != number_to_guess:
    if guess < number_to_guess:     
       print ("too low")
    else:     
       print ("too high")     
    guess = int(input("Please guess again:"))  
print ("Well done! Yes the number was", number_to_guess)


'''      
# Andrew's code
numberToGuess = 30  
guess = int(input("Please guess the number:")) 
while guess != numberToGuess:     
    if guess < numberToGuess:         
        print("too low")     
    else:          
        print("too high")     
    guess = int(input("Please guess again:"))  
print("Well done! Yes the number was ", numberToGuess)
'''