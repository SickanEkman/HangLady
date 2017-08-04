import random

def ask_letters():
    """Different ways to ask for starting letters"""
    choices = ["How many letters are in the word? \n",
               "Number of letters? \n",
               "How many letters? \n",
               "What's the word? Just kidding. How many letters? \n",
               "Number of letters in the word? \n",
               "Let's do this! How many letters? \n"]
    return random.choice(choices)

def not_int():
    """Different ways to ask for an int"""
    choices = ["Need you to write a positive number. \n",
               "Just a number, please. \n",
               "Not an integer. Try again. \n"]
    return random.choice(choices)

def prepare_game():
    """Gets number of letters"""
    num_letters = 0
    try:
        num_letters = int(input(ask_letters()))
        return num_letters
    except ValueError:
        print(not_int())
        return prepare_game()

def create_dic(num_letters):
    """Creates a dictionary with same number entries as letters in word"""
    game_d = {}
    i = 1
    while i <= num_letters:
        game_d[i] = "_"
        i += 1
    return game_d

def start_game():
    """Calls the first functions, to start a game"""
    name = input('Hi human person! What is your "name"?\n') #asks for player's name
    input("Hi " + name + "! Think of a hang-lady-type word. Okay?\n (Press enter when ready)") # greets the player
    num_letters = prepare_game() # gets the length of the word
    game_d = create_dic(num_letters) # creates suitable length dictionary with "_" values
    return game_d #returns dictionary with '_' as values

def create_corpus():
    """ID's right len words from original corpus and creates corpus dictionary"""
    corpus_d = {} # dictionary with all words with right length
    with open('./project_korpusar/only_words.conll', 'r') as fin:
        for line in fin:
            line = line.rstrip('\n')
            if len(line) == num_letters:
                line = line.lower()
                # print(line) # checks if the program works to this point
                if line not in corpus_d:
                    corpus_d[line] = 1
                else:
                    corpus_d[line] = corpus_d[line] + 1
            else:
                pass
    fin.close()
    return corpus_d

game_d = start_game() # initiates, created 
num_letters = len(game_d)
corpus_d = create_corpus()