'''
Steven Kyritsis CS100 
2021F Section 031 HW 08,
November 5, 2021
'''
#1
def two_words(length, first_letter):
    while True:
        word1 = input("Please enter a " + str(length) + "-letter word please: ")
        if len(word1) == length:
            break
    while True:
        word2 = input("Please enter a word beginnning with the letter " + str(first_letter) + " please: ")
        if word2[0].lower() == first_letter.lower():
            break