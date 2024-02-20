# grade.py
# to check that the percentage is valid
# author: Nataliia Dragunova

mark = float(input("Enter a mark: "))
if mark < 0 or mark > 100:         
   print ("Please enter a mark between 0 and 100")
elif mark >= 70: 
   print ("Distinction")
elif mark <= 69.9 and mark >= 60:
   print ("Merit 2")
elif mark <= 59.9 and mark >= 50:
   print ("Merit 1")
elif mark <= 49.9 and mark >= 40:
   print ("Pass")
else:
   print ("Fail")
'''
# Andrew's code

percentage = float(input("Enter the percentage: ")) 
#print (percentage)  
# be careful with ands and ors 
if percentage < 0 or percentage > 100:     
# Later we will show you error handling     
# This should really throw an error     
   print ("Please enter a number between 0 and 100") 
elif percentage < 40:
# we know it is greater than 0     
   print ("Fail") 
elif percentage < 50: 
# between 40 and 49     
   print ("Pass") 
elif percentage < 60: 
# between 50 and 59     
   print ("Merit1") 
elif percentage < 70: 
# between 60 and 69     
   print ("Merit2") 
else: 
# the only option left is between 70 and 100     
   print ("Distinction")
'''
