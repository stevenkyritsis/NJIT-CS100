'''
Steven Kyritsis CS100 
2021F Section 031 HW 09,
November 9, 2021
'''
#2
def file_stats(in_file):
    inFile = open(in_file)
    lines = inFile.readlines()

    w_count = 0
    l_count = 0
    ch_count = 0

    for line in lines:
        words = line.split()
        for word in words:
            if word[0].isalpha():
                w_count+= 1
                ch_count+= len(word)
        l_count+= 1    

    inFile.close()

    return 'Words: '+ str(w_count) + '\n' + 'Characters: ' + str(ch_count) + '\n' + 'Lines: ' + str(l_count)

print(file_stats('test.txt'))
        
    