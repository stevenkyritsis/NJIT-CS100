'''
Steven Kyritsis CS100 
2021F Section 031 HW 08,
November 5, 2021
'''
#3
def enter_new_password():
    num = '1234567890'
    while True:
        new_pass = input("Please enter a new password between 8-15 characters and includes 1 digit: ")
        
        if len(new_pass) < 8:
            if num not in new_pass:
                new_pass = input("Please enter a password with at least one number and with more than 7 characters: ")
            else:
                new_pass = input("Please enter a new password with more than 7 characters: ")
        if len(new_pass) > 15:
            if num not in new_pass:
                new_pass = input("Please enter a password with at least one number and less than 16 characters: ")
            else:
                new_pass = input("Please enter a new password with less than 16 characters: ")
        #if num not in new_pass: <-- this does not work for some reason
                #new_pass = input("Please enter a password with at least one number: ") <-- this does not work for some reason
        break
print(enter_new_password())