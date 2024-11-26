from random import randint

def diceroll():

    money = int(input("Enter how much money you want to gamble: "))
    maxmoney = money  # Store the initial money as maxmoney
    numofrolls = 0
    a = True

    while a:
        dice1chance = randint(1, 6)  # Roll the first die
        dice2chance = randint(1, 6)  # Roll the second die

        if money > 0:
            dice1result = dice1chance
            dice2result = dice2chance

            # Check if the sum of dice is 7, and update money accordingly
            if dice1result + dice2result == 7:
                money += 4  # Gain $4 if sum is 7
            else:
                money -= 1  # Lose $1 if sum is not 7

            # Track the maximum money held at any point
            if money > maxmoney:
                maxmoney = money

            numofrolls += 1  # Increment the number of rolls
            print(numofrolls)
        else:
            # Once the money is depleted, print the final results
            print("You are out of money!")
            print(f"It took you {numofrolls} rolls before you became broke.")
            print(f"And you only peaked at ${maxmoney} :( ")
            a = False  # Exit the loop

diceroll()
