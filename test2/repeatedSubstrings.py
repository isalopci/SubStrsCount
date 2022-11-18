import re

# Python function that identifies the substrings of 4 characters that appear 
#        along a main string of random length and content.

def generateSubStrings(originalStr: str) -> list:
    #Variable to store a list of substrings
    listSubStr = []
    
    # First loop which indicates the first index of the current substring
    for i in range(len(originalStr)-3):

        subStr = ""
        
        # Second loop to generate a 4 char substring
        for j in range(i,i+4):
            subStr += originalStr[j]

        # add substring to the list of substrings
        listSubStr.append(subStr)
    
    return listSubStr

# Python function that identifies how many substrings of 4 characters appear more
#        than once along a main string of random length and content.

def countSubStrs(originalStr: str) -> list[dict]:

    #Create an empty dictionary to store each substring with more than once instance
    subStrDict = {}
    
    #Obtains list of substrings in the original string 
    listSubStr = generateSubStrings(originalStr)

    # For each substring or 'word' in the list 
    for word in listSubStr:

        # Regular expression to get the indexes on the original string where there is an instance of the word
        listIndexes = [i.start() for i in re.finditer(word, originalStr)]

        #Number of instances
        count = len(listIndexes)

        #Adds a substring (in the dictionary) that has more than one instance in the original string
        if count > 1:
            subStrDict[word] = count

    return subStrDict


# Driver Code to test 
if __name__ == '__main__':

    originalStr = "ilovebooksoncemybooksalwaymysbooksforevermybooks"
    subStrDict = countSubStrs(originalStr)
    print(subStrDict) 
