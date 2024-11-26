from random import randint # importing random and randint for randomization
import random

def main(): # def main function
    rounds = int(input("Enter how many rounds you want the simulation to run: ")) 

# initialize variables
    correct = 0
    wrong = 0

    for i in range(rounds): # loop through rounds
        answer = random.randint(1,3) # random functions for guess and answer, 1/3 for both
        guess = random.randint(1,3)
                
        if guess == answer:
            correct += 1
        else:
            wrong += 1
#outputs
    print(f"You guessed the door with the luxary automobile {correct} times !!")
    print(f"However your win percentage was {((correct/rounds) * 100):.2f}% :(")

main()