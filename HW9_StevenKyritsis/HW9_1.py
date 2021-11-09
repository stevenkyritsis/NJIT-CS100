'''
Steven Kyritsis CS100 
2021F Section 031 HW 09,
November 9, 2021
'''
#1
def file_copy(in_file, out_file):
    inFile = open(in_file)
    outFile = open(out_file)
    contents = inFile.read()

    outFile.write(contents)

    inFile.close()
    outFile.close()