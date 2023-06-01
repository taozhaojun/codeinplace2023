import random

def main():
    # 1. Understand how to create a list and add values
    # A list is an ordered collection of values
    names = ['Chris', 'Mehran', 'Simba', 'Brahm', 'Juliette']
    names.append('Karel')

    # 2. Understand how to loop over a list
    # this prints the list to the screen one value at a time
    for value in names:
        print(value)

    # 3. Understand how to look up the length of a list
    # use randint to select a valid "index" 
    max_index = len(names) - 1
    index = random.randint(0, max_index)

    # 4. Understand how to get a value by its index
    # get the item at the chosen index
    correct_answer = names[index]

    # This is just like in Khansole Academy...
    # prompt the user for an answer, check if it is correct
    prompt = 'Who is in index...' + str(index) + '? '
    answer = input(prompt)
    if answer == correct_answer:
        print('Good job')
    else:
        print('Correct answer was', correct_answer)

if __name__ == '__main__':
    main()
    
 ####################################
def main():
    # Create a list called `fruit_list` that contains the following fruits: 'apple', 'banana', 'orange', 'grape', 'pineapple'.
    fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list.
    lst_length = len(fruit_lst)
    print(lst_length)

    # Add 'mango' at the end of the list. 
    fruit_lst.append('mango')

    # Print the updated list.
    for fruit in fruits:
        print(fruit)
 #####################################
import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    f = open(filename)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            lines.append(line)
    return lines

def play_game(words):
    while True:
        random_word = random.choice(words)
        input(random_word)

def main():
    words = get_words_from_file()
    play_game(words)

if __name__ == '__main__':
    main()
