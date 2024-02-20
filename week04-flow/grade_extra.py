# grade.py
# to check that the percentage is valid even if it is 69.9999
# author: Nataliia Dragunova


mark = float(input("Enter a mark: "))
if mark < 0 or mark > 100:         
   print ("Please enter a mark between 0 and 100")
elif round(mark,9) < 40: 
   print ("Fail")
elif round(mark,9) < 50:
   print ("Pass")
elif round(mark,9) < 60:
   print ("Merit 2")
elif round(mark,9) < 70:
   print ("Merit 1")
else:
   print ("Distinction")