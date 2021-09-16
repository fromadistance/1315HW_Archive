# Yixiao Zhang
# yzhang3739@gatech.edu
# I worked on this homework assignment alone, using only this semester's 
# course materials.


#Problem 1
def buyAVowel (puzzle,vowel,index):
  print "I'd like to buy the vowel '" + vowel + "' at index " + str(index) + "."
  print "."
  print "."
  print "."
  if vowel.lower() == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u":
    if puzzle[index].lower() == vowel.lower():
      print "Congrats! There is an '" + vowel + "' at index " + str(index) + "."
    else:
      print "Sorry, there is no '" + vowel + "' at index " + str(index) +  "."
  else:
    print "Sorry, " + vowel + " is not a vowel."
    

#Problem 2
def graduate(gpa,year,credits):
  if (gpa >=3.0 and year == 4) or (gpa >= 3.5 and year >= 3 and credits >= 90):
    print "Congratulations on graduating from Georgia Tech with a " + str(gpa) + " GPA! Go Jackets!"
  else:
    print "Sorry, you are not eligible for graduation."

#Problem 3
def driversLicense(age):
  if age >= 18: 
    print "You may obtain a Driver's License!"
  elif age >= 15 and age < 18:
    print "You may obtain a Learner's Permit. Only " + str(18-age) + " more year(s) before you can get a Driver's License!"
  else:
    print "You may not obtain a Learner's Permit. Only " + str(15-age) + " more year(s) before you can get a Learner's Permit!"

#Problem 4
def usefulLoops(times):
  while times != 0:
    print "Loops are very useful. I used a loop to write this for me."
    times = times - 1

#Problem 5
def paperSize(size):
  counter = 0
  while counter < size + 1:
    print "A" + str(counter) + " size: " + str(10000/(2**(counter))) + " square centimeters"
    counter = counter + 1
    
