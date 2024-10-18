def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for i in range(len(other_words)):
        other_words = list(other_words)
        other_words[i] = other_words[i].lower()
        if root_word in other_words[i] or other_words[i] in root_word:
            same_words.append(other_words[i])

    return same_words

rez_1 = (single_root_words('Age', 'Teenager', 'Diego', 'adjust', 'AgeLess'))
rez_2 = (single_root_words('Feedback', 'Feeder', 'Feed', 'Features', 'Fetched'))

print(rez_1)
print(rez_2)