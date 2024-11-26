def salary (startingsalary, increase, numofyears):
    totalsalary = startingsalary

    if numofyears > 10:
        numofyears = 10
    else:
        numofyears = numofyears


    for i in range(1, numofyears + 1):
        totalsalary *= (1+increase)


    return totalsalary
    
def main():
    startingsalary = int(input("Enter the starting salary: "))
    increase = float(input("Enter increase index: (0-1): "))
    numofyears = int(input("Enter how long you have been working: "))
            
    
    totalsalary = salary(startingsalary, increase, numofyears)

    print(f"You will make: {totalsalary:0.2f} This year")



main()