"""
Goal: To calculate the total of the series of single digit numbers inputted.

Description: 
Takes a users input of numbers and adds each together producing an output of all numbers combined

1. create a variable that stores the input as a list 
2. initialize a variable to calculate the total 
3. convert the values in the list to integers for calculations
4. loop through the list 
5. adding the values from the list to the variable set in step 2.
6. printing the variable when looping through the list has finished.

"""

#takes user input as a list. the input 1234 would be = ['1','2','3','4']
inputlist = list(input("Enter a series of single digit numbers: "))

total = 0  #initialize total

#converts all values in inputlist to integers for the loop
inputlist = [int(x) for x in inputlist]

#looping from 0 to the length of inputlist
for i in range(0, len(inputlist)):
    total += inputlist[i]
print(total)