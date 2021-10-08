# Yixiao Zhang
# yzhang3739@gatech.edu
# I worked on this homework assignment alone, using only this semester's
# course materials.


# Problem 1: Matching Letters
def matching(string1, string2):
    matched = ""
    list1 = []
    list2 = []
    list1 += string1
    list2 += string2
    if len(list1) <= len(list2):
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                matched += list1[i]
    else:
        for i in range(len(list2)):
            if list1[i] == list2[i]:
                matched += list2[i]
    print matched


# Problem 2: Checking Hashes
def checkHash(correctHash, attemptedHash):
    list1 = []
    list2 = []
    list1 += correctHash
    list2 += attemptedHash
    if len(correctHash) != len(attemptedHash):
        print "Hash incorrect."
        print "Hash length was " + str(len(attemptedHash)) + ", correct hash length was " + str(len(correctHash)) + "."
    else:
        if list1 == list2:
            print "Hash correct. Logged in."
        else:
            print "Hash incorrect."
            for i in range(len(list1)):
                if list1[i] != list2[i]:
                    print "Mismatch at index " + str(i) + ": got " + str(list2[i]) + ", not " + str(list1[i]) + "."


# Problem 3: Zipper
def zipper(list1, list2):
    ziplist = []
    for i in range(len(list1)):
        ziplist += [[list1[i], list2[i]]]
    print ziplist


# Problem 4: Budget
def budget(list1, list2, list3, budget):
    costList = []
    total = 0
    highestCost = 0.0
    highest = ""
    print "Shopping cart:"
    for i in range(len(list1)):
        costList += [list2[i] * list3[i]]
        total += list2[i] * list3[i]
        print list1[i] + ": " + str(list3[i]) + " x $" + str(list2[i]) + " = $" + str(costList[i])
        if costList[i] >= highestCost:
            highest = list1[i]
    if total > budget:
        print "You are over budget by $" + str(total - budget) + "."
        print "You might want to remove " + str(highest) + " from your shopping cart."
    elif total < budget:
        print "You have $" + str(budget - total) + " left to spend!"
    else:
        print "Good to check out!"


# Problem 5: Subsets
def subsets(setA, setB):
    subset = True
    for i in range(len(setA)):
        if setA[i] not in setB:
            subset = False
    if subset == True:
        print "The set " + str(setA) + " is a subset of " + str(setB) + "."
    else:
        print "The set " + str(setA) + " is not a subset of " + str(setB) + "."
