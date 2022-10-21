def HowManyEvenNumbers(num):

    # stores how many even numbers a number has
    num = int(num)
    integerCount = 0

    for i in range(1, num + 1):
        if i % 2 == 0:
            integerCount += 1

    return ("The number {} has {} Even Numbers".format(num, integerCount))
    # return integerCount

def WhatAreTheNumbers(num):

    # list containing the Even Numbers
    tempStoredNumbers = []

    for i in range(1, num + 1):
        if i % 2 == 0:
            tempStoredNumbers.append(i)

    returnInput = ", ".join(map(str, tempStoredNumbers))
    return ("And the Even Numbers are: {}".format(returnInput))

def WhatAreTheNumbersUsingArray(num):

    # Array with number values
    numbersArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # List to put in the Even Numbers
    evenNumbers = []

    for i in range(1, num + 1):
        if i % 2 == 0:
            arrayKey = numbersArray[i - 1]
            evenNumbers.append(arrayKey)

    returnInput = ", ".join(map(str, evenNumbers))
    return ("Using an Array the Even Numbers of {} are: {}".format(num, returnInput))
