# Python program that identifies how many substrings of 4 characters appear more
#        than once along a main string of random lentgh and content.

def generateSubStrings(originalStr: str):
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

# Driver Code
if __name__ == '__main__':
    originalStr = "geekslovegeeks"
    a = generateSubStrings(originalStr)
    print(a)