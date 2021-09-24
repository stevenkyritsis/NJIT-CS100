'''
Steven Kyritsis CS100 
2021F Section 031 HW 05,
October 1, 2021
'''

#1
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for month in months:
    if month[0] == 'J':
        print(month)
#2
for i in range(99):
    if i%2 == 0 and i%5 == 0:
        print(i)

#3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for letter in horton:
    if letter in vowels:
        print(letter)