def DivisibilityTest():
    MoreNumbers = True
    NumbersToCheck = []
    CheckUpTo = 1
    LooperCounter = 1
    CorrectNumbers = []
    
    print('Well hello there!\nThis is where we calculate which numbers are divisible, without going decimal on us, by two or more numbers specified by you!\n')

    while (MoreNumbers):
        NumbersToCheck.append(int(input('So which number ya wanna add?\n')))
        if (len(NumbersToCheck) >= 2):
            LoopityContinue = input('Do ya wanna add more numbers to check? Y/N \n')
            if (LoopityContinue.upper() == 'N'):
                MoreNumbers = False
            elif (LoopityContinue.upper() == 'NO'):
                MoreNumbers = False
    
    CheckUpTo = int(input('Alrighty then, which number do you want to check up to?\n'))

    while (LooperCounter <= CheckUpTo):
        CorrectNumbers.append(int(LooperCounter))
        LooperCounter += 1
    
    for Divisor in NumbersToCheck:
        LooperCounter = 0
        while(LooperCounter < len(CorrectNumbers)):
            if (CorrectNumbers[LooperCounter] % Divisor != 0):
                CorrectNumbers.pop(LooperCounter)
                LooperCounter -= 1
            LooperCounter += 1

    LastNumberToCheck = NumbersToCheck.pop()
    LastCorrectNumber = CorrectNumbers.pop()
    if (CorrectNumbers):
        print(f'And the numbers that are divisible by {str(NumbersToCheck).replace("[", "").replace("]", "")} and {LastNumberToCheck} are:\n{str(CorrectNumbers).replace("[", "").replace("]", "")} and {LastCorrectNumber}')
    else:
        print('Well somewhere along the way something went wrong and there are no numbers divisible by all of the above stated divisors within that range of numbers.\nBetter luck next time!')
    input()