import random
print("Let us guess a number selected by computer within a specific range.")
print()
print("You got 5 chances to guess the number & win")
print()

def guess():
    num = random.randrange(1, 50)
    for i in range(5):  #for limited 5 turns to play
        gnum = int(input("Guess a number between 1 and 50:\n"))
        if num<gnum:
            print("Sorry! your guess is higher, please try again with a lower number. Thanks!")
        elif num>gnum:
            print("Sorry! your guess is lower, please try again with a higher number. Thanks!")
        elif num == gnum:
            print("Congratulations! Your guess is absolutely correct.")
            break
    else:
        print("Sorry turn over! play again?")

guess()

again = input("Please enter 'y' if you want to play again\n")
while again=='y' or again =='Y':
    guess()
    again = input("Please enter 'y' if you want to play again\n")
else:
    print("Bye! Please come again.")