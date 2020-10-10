# coding: utf-8

import numpy as np

def get_reverse_map(dictionary):
    return {v:k for k,v in dictionary.items()} # Updated to python3 syntax (team1-change)

def shuffle_arrays(*arrays):
    import numpy as np
    rng_state = np.random.get_state()
    for array in arrays:
        np.random.set_state(rng_state)
        np.random.shuffle(array)
    
def input_word_index(vocabulary, input_word, unk_id, warn_unk=False):
    if warn_unk and input_word not in vocabulary:
        print(f"Warning: {input_word} not in vocabulary") # Added parenthesis and updated to f-string (team1-change)
    return vocabulary.get(input_word, unk_id)
