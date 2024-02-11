# random_fruit2.py
# program that prints out a random fruit 
# author: Nataliia Dragunova

import random # module
# tuple
fruits = ("apple","kiwi","banana","pear","appricot","orange")
# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print ("A random fruit {}".format(fruit));
