#Using a while true to make an infinite loop
while True:
    #User input stored as a float for more acurate result
    LightYear_Input = float(input("Enter a value of Light Year to be converted: "))
    #Conversion using formula
    Convert_lightYear = LightYear_Input / 0.00000000000010570
    #Printing output
    print(f"Your Light Year Value of {LightYear_Input}, is equal to: {Convert_lightYear:.2f} Kilometers")
    redo = input("Would you like to perfrom another conversion? (Y/N) ")
    #Checking if the variable redo is either y/n to either break or continue the loop
    if redo == "N" or redo == "n":
        break
    elif redo == "Y" or redo == "y":
        continue
    else: 
        print("Invalid Input: Exiting")
        break