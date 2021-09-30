# Yixiao Zhang
# yzhang3739@gatech.edu
# I worked on this homework assignment alone, using only this semester's
# course materials.


# Problem 1
def wordShift(string, num):
    count1 = 0
    text1 = ""
    count2 = 0
    text2 = ""
    while count1 < (len(string)-num):
        text1 = text1 + string[count1]
        count1 += 1
    while count2 < num:
        text2 = text2 + string[len(string)-(num-count2)]
        count2 += 1
    print text2 + text1


# Problem 2
def groceryList(groceries, item):
    print "Hello! I'm your personal list manager!"
    if item in groceries:
        print "You have '" + str(item) + "' on your grocery list!"
        print "Here's your current grocery list:"
    else:
        print "You don't have '" + str(item) + "' on your grocery list, but I will add it for you!"
        groceries += [item]
        print "Here's your new grocery list:"
    print groceries


# Problem 3
def rangePractice(num1, num2, step):
    count1 = 0
    count2 = num2
    count3 = num1
    range1 = []
    range2 = []
    range3 = []
    while count1 < num1+1:
        range1 += [count1]
        count1 += 1
    while count2 > num1-1:
        range2 += [count2]
        count2 -= 1
    while count3 < num2:
        range3 += [count3]
        count3 += step
    print "First Range:", range1
    print "Second Range:", range2
    print "Third Range:", range3


# Problem 4
def search(list, item):
    count = 0
    foundItem = []
    while count < len(list):
        if item == list[count]:
            foundItem += [count]
        count += 1
    if len(foundItem) != 0:
        for each in range(len(foundItem)):
            print "Item found at index " + str(foundItem[each]) + "."
    else:
        print "Item not found."


# Problem 5
def stats(numbers):
    sum = 0.0
    smallest = numbers[0]
    largest = numbers[0]
    for each in numbers:
        if each > largest:
            largest = each
        if each < smallest:
            smallest = each
        sum += each
    print "Mean:", sum/len(numbers)
    print "Range:", largest - smallest

