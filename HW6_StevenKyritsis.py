'''
Steven Kyritsis CS100 
2021F Section 031 HW 06,
October 1, 2021
'''

#1a
def has_final_letter(str_list, letters):
    result = []

    for item in str_list:
        if item[-1] in letters:
            result.append(item)

    return result

#1b
print(has_final_letter(['apple', 'banana', 'orange'], 'aeiou'))

print(has_final_letter(['racecar', 'paintball', 'skateboard'], 'aeiou'))

print(has_final_letter(['horse', 'goat', 'harambe'], 'eiou'))

#2a
def is_divisible(max_int, two_ints):
    for i in range(1,max_int):
        