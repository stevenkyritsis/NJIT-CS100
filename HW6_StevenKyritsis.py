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
    d_list = []
    num1 = two_ints[0]
    num2 = two_ints[1]
    for i in range(1,max_int):
        if i % num1 == 0 and i % num2 == 0:
            d_list.append(i)
    return d_list

#2b
print(is_divisible(100, (2,10)))
print(is_divisible(50, (4,5)))
print(is_divisible(20, (2,3)))