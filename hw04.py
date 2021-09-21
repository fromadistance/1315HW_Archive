# Yixiao Zhang
# yzhang3739@gatech.edu
# I worked on this homework assignment alone, using only this semester's
# course materials.

# Problem 1
def collatz(startValue):
    count = 1
    print "Starting with " + str(startValue) + "."
    while startValue != 1:
        if startValue%2 == 0:
            startValue = startValue/2
            print "Step " + str(count) + ": " + str(startValue)
        else:
            startValue = startValue * 3 + 1
            print "Step " + str(count) + ": " + str(startValue)
        count += 1
    print "It took " + str(count-1) + " steps to reach 1."


# Problem 2
def squares(n):
    count = 1
    while count != n+1:
        if (count*count) % 2 == 0:
            print str(count*count) + " is even"
        elif (count*count) % 2 != 0:
            print str(count*count) + " is odd"
        count += 1


# Problem 3
def alphabetHalves(text):
    count = 0
    countL = 0
    countR = 0
    while count != (len(text)):
        if text[count].lower() in "abcdefghijklm":
            countL += 1
            count += 1
        elif text[count].lower() in "nopqrstuvwxyz":
            countR += 1
            count += 1
        else:
            count += 1
    print "There are " + str(countL) + " first-half letters."
    print "There are " + str(countR) + " second-half letters."
    if countL > countR:
        print "First-half is better than second-half!"
    elif countL < countR:
        print "Second-half is better than first-half!"
    else:
        print "First-half and second-half are equal!"


# Problem 4
def seeingDouble(phrase):
    count = 0
    result = ""
    while count != (len(phrase)):
        result = result + phrase[count]*2
        count += 1
    print result


# Problem 5
# This method is stupid, just use (result = x + result) to simplify the procedure. :(
def spongebobTextReversed(sentence):
    count = -1
    result = ""
    if len(sentence) % 2 == 0:
        while count != -(len(sentence)) -1:
            if count % 2 != 0:
                result = result + sentence[count].upper()
                count = count - 1
            else:
                result = result + sentence[count].lower()
                count = count - 1
    else:
        while count != -(len(sentence)) -1:
            if count % 2 != 0:
                result = result + sentence[count].lower()
                count = count - 1
            else:
                result = result + sentence[count].upper()
                count = count - 1
    print result
