def some_function(word):
    space = ' ' # there is a single space between the quotes
    if space in word:
        return False
    # both letters 'A' and 'Z' are in upper case
    if not('A' <= word[0] <= 'Z'):
        return False
    for i in range(1, len(word)):
        # both letters 'a' and 'z' are in lower case
        if not('a' <= word[i] <= 'z'):
            return False
    return True

print(some_function('Vishwa'))