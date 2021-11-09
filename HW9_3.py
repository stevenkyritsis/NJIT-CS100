'''
Steven Kyritsis CS100 
2021F Section 031 HW 09,
November 9, 2021
'''
#3
def repeat_words(in_file, out_file):
    inFile = open(in_file)
    outFile = open(out_file,'w')

    lines = inFile.readlines()

    for line in lines:
        words = line.split()
        for word in words:
            if words.count(word) > 1:
                outFile.write(word+' ')

        outFile.write('\n')
    
    inFile.close()
    outFile.close()

repeat_words('test.txt', 'repeat.txt')