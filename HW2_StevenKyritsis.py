'''
Steven Kyritsis CS100 
2021F Section 031 HW 01,
September 10, 2021
'''

#1
grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']

frequency = []
frequency.append(grades.count('A'))
frequency.append(grades.count('B'))
frequency.append(grades.count('C'))
frequency.append(grades.count('D'))
frequency.append(grades.count('F'))

print(frequency)

#2
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']
hearding_dogs = dog_breeds[0:2]
tiny_dogs = dog_breeds[-1]
print(dog_breeds, hearding_dogs, tiny_dogs)
if 'Persian' in dog_breeds:
    print(True)
else:
    print(False)