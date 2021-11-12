'''
Steven Kyritsis CS100 
2021F Section 031 HW 10,
November 12, 2021
'''

#2
def initialletter(wordlist):
    my_d={}
    for word in wordlist:
        if len(word)>0:
            w=word[0]
            if w not in my_d:
                my_d[w]=[]
            if word not in my_d[w]:
                my_d[w].append(word)
    return my_d

print(initialletter(['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']))

