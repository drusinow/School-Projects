def calculatebounce (initialheight, bounceindex,  numofbounces):
    totaldistance = 0 
    currentheight = initialheight

    for i in range(numofbounces):
        totaldistance += currentheight
        currentheight *= bounceindex
        totaldistance += currentheight

    return totaldistance

def main(): 
    initialheight = float(input("Enter Initial Height of the ball: "))
    bounceindex = float(input("Enter the bounce indexx, between 0-1: "))
    numofbounces = int(input("Enter the number of bounces: "))


    total_distance = calculatebounce(initialheight, bounceindex, numofbounces)

    print(f"The total distance travelled is: {total_distance:.2f}")


main()