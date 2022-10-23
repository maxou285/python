# Trouver le mot le plus court et le plus long dans une phrase

# ordre dans la phrase en premier
def get_min_and_max_words(sentence):
    words = sentence.split()
    print(words)
    
    max_word = max(words, key=len)
    min_word = min(words, key=len)
    return min_word, max_word


s = "Un Ab sachant chasser sait chasser sans son chien"

print("Ordre dans la phrase")
min_word, max_word = get_min_and_max_words(s)
print("Mot le plus petit:", min_word)
print("Mot le plus long:", max_word)


# split()
# min max


# Trouver le mot le plus court et le plus long par ordre alphabétique
# ordre alphabétique en premier
def get_min_and_max_words_sorted(sentence):                 # 1ere Methode
    words = sentence.split(" ")
    min_word, max_word = get_min_and_max_words(sentence)

    all_min_words = [w for w in  words if len(w) == len(min_word)]
    all_max_words = [w for w in  words if len(w) == len(max_word)]

    all_min_words.sort()
    all_max_words.sort()

    return all_min_words[0], all_max_words[0]

def get_min_and_max_words_sorted2(sentence):                # 2e Methode
    words = sentence.split(" ")
    print(words)
    words.sort()
    max_word = max(words, key=len)
    min_word = min(words, key=len)
    return min_word, max_word

print("Ordre alphabétique 1ere Methode")
min_word, max_word = get_min_and_max_words_sorted(s)

print("Mot le plus petit:", min_word)
print("Mot le plus long:", max_word)


print("Ordre alphabétique 2e Methode")
min_word, max_word = get_min_and_max_words_sorted2(s)

print("Mot le plus petit:", min_word)
print("Mot le plus long:", max_word)