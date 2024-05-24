# return {sorted_word:[word]}
def sorted_words():
    words = {}
    with open("words.txt") as file:
        for line in file:
            word = line.strip()
            sorted_word = "".join(sorted(word))
            word_set = words.get(sorted_word) or set()
            word_set.add(word)
            words[sorted_word] = word_set
    return words

# return a set of anagramed words
def lookup(word):
    return sorted_words().get("".join(sorted(word))) or set()
