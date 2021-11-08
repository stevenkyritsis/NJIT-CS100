#3
def enter_new_password():
    num = '1234567890'
    while True:
        new_pass = input("Please enter a new password between 8-15 characters and includes 1 digit: ")
        if len(new_pass) < 8:
            new_pass = input("Please enter a new password with more than 7 characters: ")
        if len(new_pass) > 15:
            new_pass = input("Please enter a new password with less than 16 characters: ")
        if num not in new_pass:
            new_pass = input("Please enter a password with at least one number: ")
        else:
            break
print(enter_new_password())