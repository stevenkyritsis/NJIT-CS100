#2
def two_wordsV2(length, first_letter):
    word1 = input("Please enter a " + str(length) + "-letter word please: ")
    while len(word1) != length:
        word1 = input("Please enter a " + str(length) + "-letter word please: ")

    word2 = input("Please enter a word beginnning with the letter " + str(first_letter) + " please: ")
    while word2[0].lower() != first_letter.lower():
        word2 = input("Please enter a word beginnning with the letter " + str(first_letter) + " please: ")

print(two_wordsV2(4, 'B'))