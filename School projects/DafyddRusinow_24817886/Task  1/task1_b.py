#Function with doctest instructions, following function design recipe
def Endswith_acuk(domain):
    #takes input as a string and outputs a boolean value fo true or false
    """ (string) -> Boolean

    Returns true if the input domain ends with ".ac.uk", else returns false
    
    Endswith_acuk("example.ac.uk")
    True
    Endswith_acuk("example.com")
    False
    Endswith_acuk("sample.co.ac.uk")
    True
    Endswith_acuk("university.edu")
    False

    """
    #return statement using .endswith function to validify the domain
    return domain.endswith(".ac.uk")

#main function for input handling and proccessing
def main():
    domain = input("Enter the Domain: ")
    if Endswith_acuk(domain): #if statement to create an output
        True
        print("True")   #printing only for testing
    else:
        False
        print("False")  #printing only for testing

main() #run the main function
