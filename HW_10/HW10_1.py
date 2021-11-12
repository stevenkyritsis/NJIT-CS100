'''
Steven Kyritsis CS100 
2021F Section 031 HW 10,
November 12, 2021
'''

#1
def initialletterCount(wordlist):
    my_d={}
    for word in wordlist:
        if len(word)>0:
            w=word[0]
            if w not in my_d:
                my_d[w]=0
            my_d[w]+=1
    return my_d

print(initialletterCount(['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']))
