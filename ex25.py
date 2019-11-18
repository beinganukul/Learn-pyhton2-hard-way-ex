def break_words(stuff):
    """This function will break up wordds for us."""
    words=stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_words(words):
    """Prints the first words after poping  it off."""
    words=words.pop(0)
    print words

def print_last_word(words)
    """Prints last words after poping it off."""
    words=words.pop(-1)
    print words

def sort_sentence(sentence):
    """Takes in the full sentence and returns the sorted words."""
    words=break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence)
    words=break_words(sentence)
    print_last_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one"""
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)