import string

def check_pwd(password):
    strength = 0
    upper_count = lower_count = num_count = 0


    for char in list(password):
        if char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.digits:
            num_count += 1
         
        if upper_count > 0: 
            strength += 1
        if lower_count > 0:
            strength += 1
        if num_count > 0:
            strength += 1
        if len(password) >= 8:
            strength += 1

    if strength == 1:
        print("Password strength weak. Please enter a stronger password: ")
        return False
    elif strength == 2 or strength == 3:
        print("Password Strength Fair: Consider using more characters")
        return False
    elif strength == 4:
        print("Password strength is strong")
        return True
        

while True:
    password = input("Enter password: ")
    if check_pwd(password):
        break