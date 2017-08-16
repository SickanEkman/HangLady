import random

def ask_letters():
    """Outputs to ask for starting letters"""
    choices = ["How many letters are in the word? \n",
               "Number of letters? \n",
               "How many letters? \n",
               "What's the word? Just kidding. How many letters? \n",
               "Number of letters in the word? \n",
               "Let's do this! How many letters? \n"]
    return random.choice(choices)

def not_int():
    """Outputs to ask for an int, if ValueError"""
    choices = ["Need you to write a positive number. \n",
               "Just a number, please. \n",
               "Not an integer. Try again. \n"]
    return random.choice(choices)

def prepare_game():
    """Gets number of letters"""
    num_letters = 0
    try:
        num_letters = int(input(ask_letters()))
        return num_letters #returns number of letters in word
    except ValueError: #if ValueError, give error message and start over
        print(not_int())
        return prepare_game()

def create_dic(num_letters):
    """Creates a dictionary with same number entries as letters in word"""
    game_d = {}
    i = 1
    while i <= num_letters:
        game_d[i] = "_"
        i += 1
    return game_d #returns dictionary {1: '_', 2: '_' ...}

def start_game():
    """Calls the first functions, to start a game"""
    name = input('Hi human person! What is your "name"?\n') #asks for player's name
    input("Hi " + name + "! Think of a hang-lady-type word. Okay?\n (Press enter when ready)") # greets the player
    num_letters = prepare_game() # gets the length of the word
    game_d = create_dic(num_letters) # creates dictionary with "_" values
    return game_d #returns dictionary with '_' as values

def create_corpus():
    """ID's right len words from original corpus and creates corpus dictionary"""
    corpus_d = {}
    with open('./project_korpusar/only_words.conll', 'r') as fin:
        for line in fin:
            line = line.rstrip('\n')
            if len(line) == len(game_d): #if word in corpus is same length as game word
                line = line.lower() #remove capital letters
                if line not in corpus_d:
                    corpus_d[line] = 1 #adds entry {word: 1}
                else:
                    corpus_d[line] = corpus_d[line] + 1 #adds 1 to value = {word: 2}(1+1)
            else:
                pass #if word isn't right length - ignore the word
    fin.close()
    return corpus_d #returns a dictionary containing all words with right length

game_d = start_game() #initiates game. Gets number of letters. Creates game_d.
corpus_d = create_corpus() #creates dictionary {cow: 3, fly: 2, bug:45, ape: 10 ...}