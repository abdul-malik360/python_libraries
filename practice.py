# Write a program which randomly picks an integer from 1 to 100.
# Your program should prompt the user for guesses - if the user guesses incorrectly,
# it should print whether the guess is too high or too low. If the user guesses correctly,
# the program should print how many guess the user took to guess the right answer.
# You can assume that the user will enter valid input.


import random

number = random.randint(1, 100)
tries = 0

name = input("What's your Name? ")
name = name.strip()

print("Hello " + name + ", I'm looking for a friend.")
print("Would you like to play a game with me?")
print("1) Yes I would!")
print("2) No I'm boring")

option = input("Are we going to be friends? ")
option = int(option)

if option != 1 or 2:
    pass

if option == 1:
    print("Wow you're already amazing, thank you for saying yes")
    print("I'm thinking of a number between 1 and 100")
    print("You have 5 guess")
    print("Let The Guessing Begin!")

    guess = input("Your first guess: ")
    guess = int(guess)
    tries += 1

    if guess > number:
        print("I can't count that far, go lower")
    if guess < number:
        print("I can count a bit more than that, go higher")

    while guess != number and tries < 5:
        guess = input("You can go again: ")
        guess = int(guess)
        tries += 1

        if guess > number:
            print("Just a bit lower my friend")
        if guess < number:
            print("Just a bit higher my friend")

    if guess == number:
        print("WELL DONE my friend!!!")
        print("You only tried: " + str(tries) + " times and completed the challenge")
        print("THANKS FOR PLAYING WITH ME")


    else:
        print("I'm sorry my friend")
        print("The number was " + str(number))
        print("You ran out of guesses")


elif option == 2:
    print("Thanks for speaking to me " + name + (" have a good day!")

else:
    print("The instructions were simple " + name)
    print("JUST PICK 1 OR 2!")
