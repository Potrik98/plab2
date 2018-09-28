
def get_complete_word_list(filename: str) -> set:
    words = set()

    file = open(filename, "r")
    for line in file:
        w = line.strip()
        words.add(w)
    
    return words

def get_words_longer_than(filename: str, length=3) -> set:
    return set(filter(lambda w: len(w) > length, get_complete_word_list(filename)))
