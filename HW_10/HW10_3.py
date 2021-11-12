'''
Steven Kyritsis CS100 
2021F Section 031 HW 10,
November 12, 2021
'''

#3

def shareoneletter(wordlist):
    d={}
    for w in wordlist:
        d[w]=[]
        for i in wordlist:
            match=False
            for c in w:
                if c in i:
                    match=True
            if match and i not in d[w]:
                d[w].append(i)


    return d

print(shareoneletter(['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']))
