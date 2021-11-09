'''
Steven Kyritsis CS100 
2021F Section 031 HW 08,
November 5, 2021
'''
#4

import random

random_num = random.randrange(0,50)
print('I\'m thinking of a number in the range 0-50. You have five tries to guess it.')
for i in range(5):
    user= input('Guess ' + str(i+1) + '? ')

    if int(user) < random_num:
        print(user, ' is too low\n')
    elif int(user) > random_num:
        print(user, 'is too high\n')
    else:
        print('You are right! I was thinking of ', random_num, '!')
        break

    if i+1 == 5:
        print('The answer was', random_num,'.')