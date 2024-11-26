
def countTokens(InputTextFile): 
    f = open(InputTextFile, "r")
    text = f.read()
    tokens = text.split() # counts words/tokens using .split() function
    return len(tokens)

def countToken(InputTextFile, SearchForToken):
    f = open(InputTextFile, "r")
    text = f.read()
    SearchForToken = SearchForToken.lower() #make case insensitive
    numoftokens = text.count(SearchForToken) #assigns numoftokens to number of SearchForToken was found in text
    return numoftokens

def normalisedFrequency(tokenCount, totalwords):
    normalisedfrequencyToken = tokenCount / totalwords # uses already defined return from previous function to calculate frequency
    return normalisedfrequencyToken

def sentenceCount(InputTextFile):
    f = open(InputTextFile, "r")
    text = f.read()
    stops = text.split(".") + text.split("?") + text.split("!") # splits text into 'sentences' by spliting at any '.', '?', or '!'. -> not 100% accurate
    sentences = len(stops) 
    return sentences


def sentencesContaining(InputTextFile, SearchForToken):
    f = open(InputTextFile, "r")
    text = f.read()
    #lower to not make it case sensitive
    SearchForToken = SearchForToken.lower()
    sentences = text.split(".")
    #create list variable to store all sentences containing the word, can convert to string later to format output
    sentenceswithtoken = []
    #loop through sentences
    for sentence in sentences:
        if SearchForToken in sentence.lower(): # lower to make case insensitive
            sentenceswithtoken.append(sentence.strip()) # append sentence to list. 
    return sentenceswithtoken

#Creating a main function to make readabilty and organization better. InputTextFile and SearchForToken can be used multiple times too.
def main():
    #assigning variables to function return for output/printing
    InputTextFile = str(input("Enter the file name of the text (should include the file name extension): "))
    SearchForToken = str(input("Enter a token/word you would like to search for in the text: "))
    totalwords = countTokens(InputTextFile)
    tokenCount = countToken(InputTextFile, SearchForToken)
    normalisedFreq = normalisedFrequency(tokenCount, totalwords)
    numofsentences = sentenceCount(InputTextFile)
    sentenceswithtoken = sentencesContaining(InputTextFile, SearchForToken)

    #Print statements to valitify functionality.
    print(f"Total words/tokens: {totalwords}")
    print(f"Number of occuurences of '{SearchForToken}': {tokenCount}")
    print(f"Normalised freequency of '{SearchForToken}': {normalisedFreq:.4f}")
    print(f"The number of sentences in '{InputTextFile}' is: {numofsentences}")
    print(f"The following are all sentences containing the word: '{SearchForToken}' :\n" + "\n".join(sentenceswithtoken))   #used .join to maek formating easier and converts the variable sentenceswithtoken(a list), to a string

main()
