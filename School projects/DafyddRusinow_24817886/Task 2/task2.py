# Creating a variable to store categories of the index : this is a list that stores tuples
bmi_categories = [
    ((0, 18.4), "Underweight"),
    ((18.5, 24.9), "Healthy"),
    ((25.0, 29.9), "Overweight"),
    ((30, float("inf")), "Obese")   # uses float("inf") to set no upper limit
]
# main function
def main (): 
    f = open("bmi.csv", "a")    # opens the bmi.csv file, if it is not found it will create one. Appened used.

#variable inputs
    name = str(input("Enter your first name: "))
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    #Calculation -> heigh/100 to change from cm to m
    bmi = weight / ((height/100) ** 2)

    #initializing the category vartiable
    categorization = ""

    # simple loop to assign the index to a category 
    for (Lower_Bound, Higher_Bound), category in bmi_categories:
        if Lower_Bound <= bmi <= Higher_Bound:
            categorization = category

    #piecing it together to produce the output | :.2f used to round to the second float point.
    Info_List = (f"{name}, {height}, {weight}, {bmi:.2f}, {categorization}\n")

    #write to the file  
    f.write(Info_List)
    
#run the function :D
main()

