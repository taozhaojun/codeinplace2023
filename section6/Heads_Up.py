#version 1 using list
import random
# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    f = open(FILE_NAME)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            lines.append(line)
    return lines
def main():
    # your code here :) 
    words = get_words_from_file()
    max_index = len(words) - 1
    # using a list to check if the word has been used or not
    index_shown = []
    
    while True:
        input("Press Enter to show a word")
        index = random.randint(0, max_index)
        #repeated until we find a word which is not used
        while index in index_shown:
            index = random.randint(0, max_index)
            
        index_shown.append(index)
        word_chosen = words[index]
        print(word_chosen)
        # check if all the words have been used
        if len(index_shown)-1==max_index:
            print("all the words are used")
            return
if __name__ == '__main__':
    main()
    
# version 2: using dict
import random
from collections import Counter

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    f = open(FILE_NAME)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            lines.append(line)
    return lines


def main():
    # your code here :) 
    words = get_words_from_file()
    dict_words = Counter(words)
    max_index = len(words) - 1
    count = 0
    while True:
        input("Press Enter to show a word")
        index = random.randint(0, max_index)
        word_chosen = words[index]
        #check if word_chosen has been used:
        while dict_words[word_chosen] == 0:
            index = random.randint(0, max_index)
            word_chosen = words[index]
        print(word_chosen)
        dict_words[word_chosen] -= 1
        count += 1
        if count-1 == max_index:
            print("all the words are used")
            #print(Counter(dict_words))
            return
    
if __name__ == '__main__':
    main()
