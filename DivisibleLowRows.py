#def DivisibilityTest():
NumbersToCheck = []
CorrectNumbers = []
LooperCounter = 1
NumbersToCheck.append(int(input('Well hello there!\nThis is where we calculate which numbers are divisible, without going decimal on us, by two numbers specified by you!\nLet\'s start with the first number:\n')))
NumbersToCheck.append(int(input('And the second number?\n')))
while (LooperCounter <= 1000):
    if (LooperCounter % NumbersToCheck[0] == 0):
        CorrectNumbers.append(LooperCounter)
    LooperCounter += 1
while (LooperCounter - 1001 < len(CorrectNumbers)):
    if (CorrectNumbers[LooperCounter - 1001] % NumbersToCheck[1]):
        CorrectNumbers.pop(LooperCounter - 1001)
    else:
        LooperCounter += 1
if (CorrectNumbers):
    print(f'And the numbers that are divisible by {str(NumbersToCheck[0])} and {str(NumbersToCheck[1])} are:\n{str(CorrectNumbers)}')
else:
    print('Well somewhere along the way something went wrong and there are no numbers divisible by all of the above stated divisors within that range of numbers.\nBetter luck next time!')
input()