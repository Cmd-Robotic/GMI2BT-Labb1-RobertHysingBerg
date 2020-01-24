from random import randint as RandomNumberGod

def UserGuessesNumber():
    print('So ya wanna guess what number I\'m thinking of eh?\n')
    StartNumber = int(input('Between which numbers should the guess be, eh?\nStart with the lowest one please\n'))
    EndNumber = int(input('And the other number if you would be so kind?\n'))
    Guess = int(input('Well then, take a wild guess!\n'))
    ThinkNumber = RandomNumberGod(StartNumber, EndNumber)
    
    while (Guess != ThinkNumber):
        if (Guess > ThinkNumber):
            Guess = int(input('HA! That ain\'t it laddie! That number was too large!\n'))
        elif (Guess < ThinkNumber):
            Guess = int(input('HA! That ain\'t it laddie! That number was too small!\n'))
    print('Well ya got me there laddie...')
    input()

def PCGuessesNumber():
    print('Alrighty, then pick a number and I\'ll guess!\nBut first I\'ll need some input from you between which numbers it lies\nNow enter the smallest number which your guess is between:')
    SmallestNumber = int(input())
    LargestNumber = int(input("Allright, then what's the largest number?\n"))
    Guess = True
    NewGuess = int((SmallestNumber + LargestNumber) / 2 + RandomNumberGod(-1, 1) * RandomNumberGod(0, int((SmallestNumber + LargestNumber)/4)))
    while (Guess):
        Answer = input(str(NewGuess) + ' is this yer number? Y/N\n')

        if (Answer.upper() != 'Y' and Answer.upper() != 'YE' and Answer.upper() != 'YES'):
            LowerNumber = input('Allrighty, was yer number larger than the one I guessed? Y/N\n')
        
            if (LowerNumber.upper() == 'Y' or LowerNumber.upper() == 'YE' or LowerNumber.upper() == 'YES'):
                SmallestNumber = NewGuess
                OldGuess = NewGuess

                while (OldGuess >= NewGuess or NewGuess < SmallestNumber or NewGuess > LargestNumber):
                    NewGuess = int((SmallestNumber + LargestNumber) / 2 + RandomNumberGod(-1, 1) * RandomNumberGod(0, int((SmallestNumber + LargestNumber)/4)))
            else:
                LargestNumber = NewGuess
                OldGuess = NewGuess

                while (OldGuess <= NewGuess  or NewGuess < SmallestNumber or NewGuess > LargestNumber):
                    NewGuess = int((SmallestNumber + LargestNumber) / 2 + RandomNumberGod(-1, 1) * RandomNumberGod(0, int((SmallestNumber + LargestNumber)/4)))
        else:
            Guess = False
    print('Hah! I guessed yer number! Choose a better wun next time then laddie!')
    input()