# HW1
#Due Date: 09/11/2020, 11:59PM
"""                                   
### Collaboration Statement:
             
"""
def rectangle(perimeter,area):
    """
        Returns the longest side of the rectangle with given perimeter and area 
        if both sides are integer lengths

        Doctest:
            >>> rectangle(14, 10) # From a 2x5 rectangle
            5
            >>> rectangle(12, 5) # From a 1x5 rectangle
            5
            >>> rectangle(25, 25) # A 2.5x10, but one side is not an integer
            -1
            >>> rectangle(50, 100) # From a 5x20 rectangle
            20
            >>> rectangle(11, 5)
            -1
            >>> rectangle(11, 4)
            -1
    """
    areas = []

    # Starting at 1 going until half the area
    for i in range(1, int( area / 2 )):

        # If the area divided by the iterable is an integer
        if type(area // i) == int:

            # Ensure the quotient == the area
            if ( area // i ) * i == area:

                # Add possible area values
                areas.append([i,area // i])
        else:
            return -1

    # Find which area combo results in the correct perimeter
    for j in range(len(areas)):

        # Find the perimeter of the combo and comapre it to the given perimeter
        if (areas[j][0] * 2) + (areas[j][1] * 2) == perimeter:

            # This combo matches the perimeter, at index j, return longest side
            if areas[j][0] > areas[j][1]:
                return areas[j][0]

            else:
                return areas[j][1]
    else:
        return -1

# Find any special characters and put them at their own index

def separateChars(aList):
    '''
        Separate Special Characters
        ~~~~
        The goal of this function is to find special characters, remove them from the original str, 
        and add both the str w/o the special character and the special character to their own index 
        of the list while preserving the chronoglogical order of the indices

        * The input list must be a list of strings

        Doctest:
            >>> aList = ['Hey','(Hi)','my','name;','is']
            >>> separateChars(aList)
            ['Hey','(','Hi',')','my','name',';','is']

        ### Collaboration Statement:
            I worked on this subfunction (separateChars) alone, using only this semester's course materials
    '''
    # Define all special characters
    specChar = [',','.','/','?',';',':','(',')','*','&','^','%','$','#','@','!','`','~','=','+','_','-','\\','|','<','>','[',']','{','}']

    lst = []
    x = 0
    y = 0

    # Iterate through all indices in given list
    for i in range(len(aList)):
        
        # Iterate through all special characters
        for j in range(len(specChar)):

            # If a special character is found within the str
            if specChar[j] in aList[i]:

                newStr = ''
                newLst = []

                # Find the index/indicies within the string that have a special character
                for k in range(len(aList[i])):

                    # Iterate through all special characters
                    for l in range(len(specChar)):

                        # Create sub list for the chars within the str

                        # Special character at this index of the str
                        if aList[i][k] == specChar[l]:

                            # If there is length to the new str, then there are chars before the special character
                            if len(newStr) > 0:

                                newLst.append(newStr)
                                newLst.append(specChar[l])

                            else:
                                # Otherwise just add the special character
                                newLst.append(specChar[l])

                        # No special character, add back to str -- control structure
                        else:
                            y += 1

                    # Append control structure
                    if y > 0:

                        # Check if there are prior special characters in the str
                        if aList[i][k].isalnum():

                            newStr += aList[i][k]                

                # Add the sub list to the index of lst
                lst.append(newLst)
                x = 0
                break

            # No special character, just add it back to new list -- control structure
            else:
                x += 1

        # Append control structure
        if x > 0:
            lst.append(aList[i])


    print(lst)

############################################
'''
                # Find the index of the special character within the str 
                for k in range(len(aList[i])):

                    # Special character at index k
                    if aList[i][k] == specChar[j]:

                        # Remove the special character
                        newStr = ''

                        # Add every index except the one with the special character
                        for l in range(len(aList[i])):
                            
                            # Skip the index with the special character
                            if l != k:

                                newStr += aList[i][l]

                        if newStr.isalnum() == False:

                            fixedStr = ''

                            while newStr.isalnum() == False:

                                for o in range(len(newStr)):

                                    for p in range(len(specChar)):

                                        if newStr[o] == specChar[p]:

                                            # Add every index except the one with the special character
                                            for q in range(len(newStr)):
                                                
                                                # Skip the index with the special character
                                                if q != o:

                                                    fixedStr += newStr[q]
                                
                                newStr = fixedStr

                        print(newStr)

                        # Add str w/o special character / add special character
                        newList = []

                        # Append all indicies up to the index were working on
                        for m in range( len(aList) - (len(aList)-i) ):

                            newList.append(aList[m])

                        # The special character is at the beginning
                        if k == 0:
                            print('k==0')
                            print(specChar[j], newStr)
                            # Append the special character then the rest of the string
                            lst.append(specChar[j])
                            lst.append(newStr)
                            print(newList,'\n')
                            
                        # The special character is at the end
                        elif k == (len(aList[i])-1):
                            print('k is at the end')
                            print(newStr, specChar[j])
                            # Append the string, then the special character
                            lst.append(newStr)
                            lst.append(specChar[j])     
                            print(newList,'\n')

    print(lst)
           '''
# TODO: FINISH THIS
def translate(dict_words, txt):
    """
        Translates all words in the input string that have an entry in the given translation dictionary

        Doctest:
            >>> myDict = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} 
            >>> text = '1 UP, 2 down / left right forward' 
            >>> translate(myDict, text)
            '2 down 2 up right left forward'
            >>> text
            '1 UP, 2 down / left right forward'
            >>> translate({'a':'b'}, text)
            '1 up 2 down left right forward'
    """

    newStr = ''
    print(txt)
    # Split over whitespace
    txt = str(txt).split()

    for i in range(len(txt)):

        if txt[i] in dict_words:

            print(txt[i].lower(), dict_words[txt[i].lower()])

            newStr += dict_words[txt[i]]
            newStr += ' '

        elif txt[i].upper() in dict_words:

            print(txt[i].lower(), dict_words[txt[i].lower()])

            newStr += dict_words[txt[i].upper()]
            newStr += ' '

        elif txt[i].lower() in dict_words:

            print(txt[i].lower(), dict_words[txt[i].lower()])

            newStr += dict_words[txt[i].lower()]
            newStr += ' '
        
        else:

            newStr += txt[i]
            newStr += ' '
                
    return newStr


########################################

    # newTxt = ''

    # # Split the string over spaces
    # txt = str(txt).split()

    # # Find any special characters and put them at their own index

    # # For the length of the list
    # for i in range(len(txt)):

    #     print('eval:', txt[i])

    #     # For all the words in the string that are found in the dict
    #     if txt[i] in dict_words:
    #         print('adding')
    #         newTxt += dict_words[txt[i]]
    #         newTxt += ' '

    #     elif txt[i].upper() in dict_words:
    #         print('adding u')
    #         newTxt += dict_words[txt[i].upper()]
    #         newTxt += ' '

    #     elif txt[i].lower() in dict_words:
    #         print('adding l')
    #         newTxt += dict_words[txt[i].lower()]
    #         newTxt += ' '

    # return newTxt

######################################
# def successors(file):
#     """
#         Opens a text file and creates a dictionary whose keys are words from the text file 
#         and whose values are lists of words that immediately follow the key word.

#         Doctest:
#             >>> expected = {'.': ['He', 'But', '(', ')'], 'He': ['will'], 'will': ['be', 'see'], 'be': ['the'], 'the': ['president', 'company', 'importance'], 'president': ['of', '.'], 'of': ['the', 'it', 'these'], 'company': [';'], ';': ['right'], 'right': ['now'], 'now': ['he'], 'he': ['is', ',', 'will'], 'is': ['a', 'no'], 'a': ['vice'], 'vice': ['president'], 'But': ['he'], ',': ['himself', 'is'], 'himself': [','], 'no': ['sure'], 'sure': ['of'], 'it': ['.'], '(': ['Later'], 'Later': ['he'], 'see': ['the'], 'importance': ['of'], 'these': ['3'], '3': ['.']}
#             >>> returnedDict = successors('article.txt')
#             >>> expected == returnedDict
#             True
#             >>> returnedDict['the']
#             ['president', 'company', 'importance']
#             >>> returnedDict['will']
#             ['be', 'see']
#             >>> returnedDict['3']
#             ['.']
#             >>> returnedDict['.']
#             ['He', 'But', '(', ')']
#             >>> successors('article.tt') is None
#             True
#             >>> successors(2.3) is None
#             True
#     """
#     # --- YOU INPUT VALIDATION STARTS HERE

#     dictionary = { '.' : [] }
#     specChar = [',','.','/','?',';',':','(',')','*','&','^','%','$','#','@','!','`','~','=','+','_','-','\\','|','<','>','[',']','{','}']

#     # Input check
#     if type(file) != str:
#         return None

#     # Open the file and read the contents
#     with open(file) as f:   # with ensures the file is properly closed after its suite finishes, even if an error ocurred
#         contents = f.read() # use the read() function to read the entire file, contents has the data as string

#         contents = contents.split()
#         newContents = []
#         x = 0

#         # Get the contents of the file organized

#         for i in range(len(contents)):

#             for j in range(len(specChar)):

#                 # Check each special character
#                 if specChar[j] in contents[i]:

#                     # Set control loop condition
#                     x = 0
#                     break

#                 else:
#                     # Set control loop condition
#                     x += 1
            
#             if x > 0:
#                 # Everything in this indices string is alnumeric, just add it back
#                 newContents.append(contents[i])

#             if x == 0:
#                 # The length of the string
#                 for k in range(len(contents[i])):

#                     # The special character is at the str index k
#                     if contents[i][k] == specChar[j]:
                        
#                         # Set control loop condition
#                         x = 0

#                         # Remove the character and append the str w/o the character
#                         newStr = contents[i].replace( contents[i][k], '' )

#                         newContents.append(newStr)

#                         # Append the special character to the list at its own index
#                         newContents.append(specChar[j])
                            
#             # Each index should be either all alnum or not alnum, check for ['3)'] instance, any non alnum should be len 1
#             if contents[i].alnum() == False and len(contents[i]) != 1:
            
#                 for l in range(len(contents[i])):

#                     for m in range(len(specChar)):

#                         # Check each special character
#                         if specChar[j] in contents[i]:

#             print('\n',newContents)


def sumDigits(num):
    """
        >>> sumDigits(1001)
        2
        >>> sumDigits(59872)
        31

    """
    #- YOUR CODE STARTS HERE
    pass



def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(3.5)
        >>> hailstone(0)
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    """
    
    #- YOUR CODE STARTS HERE
    pass


def common(aList1, aList2):
    """
        >>> common([12,3,5,8,90,11,44,66,8,9,34,56,-1,0,5,3333,3,2,1],[12,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,44])
        [1, 3, 12, 44]
        >>> common([1,2,3],[4,5,6])
        []
        >>> common(1, [3.5]) is None
        True
    """
    #- YOU CODE STARTS HERE


if __name__ == "__main__":

    # successors('C:\\Users\\Domin\\github\\CMPSC-132\\Hw 1\\article.txt')

    separateChars(['Hey','(Hi)','my','name;','is'])

    # print(translate({'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'}, '1 UP, 2 down / left right forward'))
    
    # import doctest
    # doctest.testmod()