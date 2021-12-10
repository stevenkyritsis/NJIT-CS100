'''
Steven Kyritsis
CS100-031 Fall 2021
HW12 December 10, 2021
'''

#1
def safeOpen(inFile):
    try:
        file = open(inFile)
        return file
    except:
        return None

#2
def safeFloat(inFloat):
    try:
        newFloat = float(inFloat)
        return newFloat
    except ValueError:
        return 0.0

#3
def averageSpeed():
    count = 0
    while (count < 2):
        inFile = input('Please input a file: ')
        file = safeOpen(inFile)
        if file = None:
            count += 1
        else:
            break

    contents = file.read()
    lst = contents.split()
    for item in lst:
        if safeFloat(item) > 2.0:
            accum += safeFloat(item)
    avg = accum / len(lst)
    return avg