# guess1.py
# that prompts the user to guess a number, 
# the program should keep prompting the user to guess the number until the user gets the right on 
# author: Nataliia Dragunova

guess = int(input("Please guess the number: "))
while guess != 33:
    if guess != 33:
      print ("Wrong")
    guess = int(input("Please guess again: "))
else:
   print ("Well done! Yes the number was 33")

'''       
# Andrew's code

numberToGuess = 30  
guess = int(input("Please guess the number:")) 
while guess != numberToGuess:     
    print ("Wrong")     
    guess = int(input("Please guess again:"))  
print ("Well done! Yes the number was ", numberToGuess)
'''