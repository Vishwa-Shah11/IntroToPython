def distance(word_1, word_2):
    word_distance = 0
    if (len(word_1) != len(word_2)):
        word_distance = -1
    else:
        for i in range(len(word_1)):
            d = abs((ord(word_1[i]) - ord(word_2[i])))
            word_distance += d
    return word_distance

print(distance('dog', 'cat'))