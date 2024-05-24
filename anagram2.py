# initially calculate score_table
score_table = {}
for letter in {'a', 'e', 'h', 'i', 'n', 'o', 'r', 's', 't'}:
    score_table[letter] = 1
for letter in {'c', 'd', 'l', 'm', 'u'}:
    score_table[letter] = 2
for letter in {'b', 'f', 'g', 'p', 'v', 'w', 'y'}:
    score_table[letter] = 3
for letter in {'j', 'k', 'q', 'x', 'z'}:
    score_table[letter] = 4

# return (word, socre, dict{letters:count})
def get_entry(word):
    letters = {}
    score = 0
    for letter in word:
        letters[letter] = (letters.get(letter) or 0) + 1
        score += score_table[letter]
    return (word, score, letters)

# return a list of (word, score, dict{letter:count})
#   in a dscending order of scores
def sorted_words():
    words = []
    with open("words.txt") as file:
        for line in file:
            word = line.strip()
            words.append(get_entry(word))
    return sorted(words, key=lambda x: x[1], reverse=True)

#initially calculate words
words = sorted_words()

# get the anagram with the highest score
def lookup(tgt):
    letters = {}
    for letter in tgt:
        letters[letter] = (letters.get(letter) or 0) + 1
    for word in words:
        complete_flag = True
        for letter, cnt in word[2].items():
            if (letters.get(letter) or 0) < cnt:
                complete_flag = False
                break
        if complete_flag:
            return word[0]
    return None

# manage files
def get_anagrams(fname):
    new_fname = fname[:fname.find(".")] + "_anagrams.txt"
    with open(new_fname, "w") as new_file:
        with open(fname) as file:
            for line in file:
                tgt = line.strip()
                new_file.write(lookup(tgt) + "\n")
