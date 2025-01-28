# adding this to allow commenting for reviewers
def build_markov_model(markov_model, new_text):
    '''
    Function to build or add to a 1st order Markov model given a string of text
    We will store the markov model as a dictionary of dictionaries
    The key in the outer dictionary represents the current state
    and the inner dictionary represents the next state with their contents containing
    the transition probabilities.
    Note: This would be easier to read if we were to build a class representation
           of the model rather than a dictionary of dictionaries, but for simplicitiy
           our implementation will just use this structure.

    Args:
        markov_model (dict of dicts): a dictionary of word:(next_word:frequency pairs)
        new_text (str): a string to build or add to the moarkov_model

    Returns:
        markov_model (dict of dicts): an updated markov_model

    Pseudocode:
        Add artificial states for start and end
        For each word in text:
            Increment markov_model[word][next_word]

    '''
# adding this to allow commenting for reviewers
    def add_pair(first_pair, second_pair):
        if (first_pair in markov_model):
            markov_model[first_pair][second_pair] = 1
        else:
            markov_model[first_pair] = {second_pair: 1}

    text = new_text.split(" ")
    for count in range(0, len(text)):
        if (count == 0):
            add_pair('*S*', text[count])
            add_pair(text[count], text[count + 1])
        elif (count == len(text) - 1):
            add_pair(text[count], '*E*')
        else:
            add_pair(text[count], text[count + 1])
    return markov_model

markov_model = dict()
text = "one fish two fish red fish blue fish"
markov_model = build_markov_model(markov_model, text)
print (markov_model)

import numpy as np

# adding this to allow commenting for reviewers
def get_next_word(current_word, markov_model, seed=42):
    '''
    Function to randomly move a valid next state given a markov model
    and a current state (word)

    Args:
        current_word (tuple): a word that exists in our model
        markov_model (dict of dicts): a dictionary of word:(next_word:frequency pairs)

    Returns:
        next_word (str): a randomly selected next word based on transition probabilies

    Pseudocode:
        Calculate transition probilities for all next states from a given state (counts/sum)
        Randomly draw from these to generate the next state

    '''
    word_list = []
    freq_list = []
    np.random.seed(seed)
    for i in markov_model:

        if current_word == i or current_word in i:  # handles both tuple or singular words
            word_list.extend(markov_model[i].keys())
            freq_list.extend(markov_model[i].values())
    prob = [x / sum(freq_list) for x in freq_list]
    random_word = np.random.choice(word_list, p=prob)
    return random_word

# adding this to allow commenting for reviewers
def generate_random_text(markov_model, seed=42):
    '''
    Function to generate text given a markov model

    Args:
        markov_model (dict of dicts): a dictionary of word:(next_word:frequency pairs)

    Returns:
        sentence (str): a randomly generated sequence given the model

    Pseudocode:
        Initialize sentence at start state
        Until End State:
            append get_next_word(current_word, markov_model)
        Return sentence# adding this to allow commenting for reviewers

    '''
    # adding this to allow commenting for reviewers
    scentence = []
    np.random.seed(seed)

    order = 0
    start_state = '*S*'
    for i in markov_model:
        if start_state in i:
            order = len(i)
            break

    init_start_state = ('*S*',) * order

    for _ in range(len(markov_model)):  # number of iteration found in the markov model
        words_to_connect = (get_next_word(init_start_state, markov_model, seed))
        if words_to_connect == '*E*':
            break
# adding this to allow commenting for reviewers
        scentence.append(words_to_connect)
        init_start_state = (*init_start_state[1:], words_to_connect)
    return ' '.join(scentence)

markov_model = dict()
# Read in the whole book
# An example of a more complex text that we can use to generate more complex output

file = open("data/one_fish_two_fish.txt", "r")
fishies = ""
for line in file:
    line = line.strip()
    fishies = fishies + ' ' + line
markov_model = build_markov_model(markov_model, fishies, order=6)

print (generate_random_text(markov_model,seed=7))

sonet_markov_model = dict()
file = open("data/sonnets.txt", "r")
sonet = ""
for line in file:
    line = line.strip()
    if line == "":
        # Empty line so build model
        sonet_markov_model = build_markov_model(sonet_markov_model, sonet, order=2)
        sonet = ""
    else:
        sonet = sonet + ' ' + line
# adding this to allow commenting for reviewers
print(generate_random_text(sonet_markov_model, seed=7))

# tryign to making a pull request testing
