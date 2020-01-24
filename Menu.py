from DivisibleBy import DivisibilityTest as YaWannaDivideSomeNumbersEh
from NumberGuess import UserGuessesNumber as GuessTimeForUser
from NumberGuess import PCGuessesNumber as PCGuessesBetter

def MenuMenu():
    ExitCondition = True
    while(ExitCondition):
        print('Allright, here\'s yer options laid out fer ya\n1. Check divisors\n2. Guess a number\n3. I guess a number\n4. Exit the program\n')
        try:
            UserChoice = input('So what\'cha gonna do?\n')
        except:
            UserChoice = 0

        if (UserChoice == '1' or UserChoice == '1.' or UserChoice == '1. '):
            try:
                YaWannaDivideSomeNumbersEh()
            except:
                print('Something went wrong, ok?')
        elif(UserChoice == '2' or UserChoice == '2.' or UserChoice == '2. '):
            try:
                GuessTimeForUser()
            except:
                print('Something went wrong, ok?')
        elif(UserChoice == '3' or UserChoice == '3.' or UserChoice == '3. '):
            try:
                PCGuessesBetter()
            except:
                print('Something went wrong, ok?')
        elif(UserChoice == '4' or UserChoice == '4.' or UserChoice == '4. '):
            ExitCondition = False
        else:
            print('Well I can\'t tell what yer sayin\' so I\'m kicking ya back to dem choices.\n')