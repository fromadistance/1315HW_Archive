# Yixiao Zhang
# yzhang3739@gatech.edu
# I worked on this homework assignment alone, using only this semester's 
# course materials.

# PROBLEM 1
def predictNotes(class1,class2,class3,class4):
  print (class1 + class2 + class3 + class4)/4.0 + 1

# PROBLEM 2
def hiddenCode(code1,code2):
  print "You said: \"" + code1[0] + code2[0] + code1[len(code1)/2] + code2[len(code2)/2] + code1[-1]+code2[-1] + "\""

# PROBLEM 3
def tired(yawn): 
  print "Tired-o-meter: " + str(len(yawn) - 3) + " yawn units"

# PROBLEM 4
def rideHeight(height,heightReq,rideName):
  if height >= heightReq:
    print "Yes, you can ride " + rideName + "!"
  else:
    print "Sorry, you must be at least " + str(heightReq) + " inches tall to ride " + rideName + "."

# PROBLEM 5
def startsAndEndsWith(name):
  if name[0].lower() == name[-1].lower():
    print name + " starts and ends with the letter " + name[0] + "!"
  else:
    print name + " starts with the letter " + name[0] + " but ends with the letter " + name[-1] + "."

