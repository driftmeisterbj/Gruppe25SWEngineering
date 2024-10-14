import csv

def resetCSV(filename):
    with open(filename+".csv", "w", newline="") as file:
        writer = csv.DictWriter(file, ["username", "password", "email"])
        writer.writeheader()


def is_username_taken(username, filename):
    listOfUsernames = []
    with open(filename+".csv", "r") as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            listOfUsernames.append(line[0])

    if username.lower() in listOfUsernames:
        return True
    else:
        return False

def is_username_valid(username):
    is_valid = True
    illegal_chars=["'", '"', ",", "!", "@", "$", "€", "{", "}",
                 "[", "]", "(", ")", "^", "¨", "~", "*", ".",
                 "&", "%", "¤", "#", "!", "?", "+", " "]
    
    if len(username) < 3:
        is_valid = False
        print(f'Name: "{username}" failed - Username can not be shorter than 3 characters')

    elif len(username) > 25:
        is_valid = False
        print(f'Name: "{username}" failed - Username can not be longer than 25 characters')

    else:
        for char in username:
            if char in illegal_chars:
                is_valid = False
                print(f'Username contains illegal character: " {char} "')

    return is_valid

def is_password_valid(password):
    is_valid = False   
    contains_uppercase = False
    contains_lowercase = False
    contains_number = False

    if len(password) < 4:
        print("Password cannot be shorter than 4 characters")

    elif len(password) > 45:
        print("Password cannot be longer than 45 characters")

    else:
        for char in password:
            if char.isupper():
                contains_uppercase = True
            if char.islower():
                contains_lowercase = True
            if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                contains_number = True
    
    if (contains_uppercase and contains_lowercase and contains_number):
        is_valid = True

    return is_valid

def is_email_taken(email, filename):
    listOfEmails = []
    with open(filename+".csv", "r") as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            listOfEmails.append(line[2])

    if email.lower() in listOfEmails:
        return True
    else:
        return False
    
def is_email_valid(email):
    is_valid = False
    contains_at = False
    contains_punctuation = False
    contains_no_duplicates = False
    contains_only_legal_chars = True
    legalPunctuationAfterAt = False

    illegal_chars=["'", '"', ",", "!", "$", "€", "{", "}",
                 "[", "]", "(", ")", "^", "¨", "~", "*",
                 "&", "%", "¤", "#", "!", "?", "+", " "]
    
    for char in email:  
        if char in illegal_chars:
            contains_only_legal_chars = False
            print(f'ERROR - Illegal character " {char} " in email adress')
           
    contains_punctuation = True
    contains_no_duplicates = True
    if email.count("@") > 0:
        contains_at = True
        if email.count("@") == 1:
            if email.count(".") > 0:
                contains_punctuation = True
                contains_no_duplicates = True
            else:
                print('Email MUST contain the character " . "')
        else:
            print('Email contains too many instances of the char " @ ", you can only use this character ONCE')
    else:
        print('Email MUST contain the character " @ "')

    if contains_at and contains_punctuation and contains_no_duplicates and contains_only_legal_chars:
        charList = []
        for char in range(email.index("@"), len(email)):
            charList.append(email[char])

        print(charList)
        if charList.count(".") > 1:
            print('ERROR - There can only be a single instance of the character " . " after the " @ "')
        
        else:
            punctuation_last_index = 0
            counter = 0
            
            for char in email:
                if char == ".":
                    punctuation_last_index = counter    
                counter += 1

            if punctuation_last_index < email.index("@"):
                print('ERROR - The character MUST appear at least once after the character " @ " in the email adress')
            else:
                is_valid = True

    return is_valid

    
    

def addUserToCSV(filename, username, password, email):
    if is_username_valid(username):
        if is_username_taken(username, filename) == False:
                if is_password_valid(password):
                    if is_email_valid(email):
                        if is_email_taken(email, filename) == False:
                                with open(filename+".csv", "a", newline="") as file:
                                    writer = csv.DictWriter(file, ["username", "password", "email"])
                                    writer.writerows([{"username": username.lower(), "password": password, "email": email.lower()}]) 
                        else:
                            print("An account with this email adress already exists")
                    else:
                            print("Email is invalid. Check error messages in console.")
                else:
                    print("Password is invalid - Password must contain an uppercase letter, a lowercase letter and a number")
        else:
            print("Username is already taken")
    else:
            print("Username is invalid. Check error messages in console.")



def readCSV(filename):
    with open(filename+".csv", "r") as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            print(line)

"""
resetCSV("userdb")
addUserToCSV("userdb", "Test1", "Passord123", "ma!i?l@mail.com")
addUserToCSV("userdb", "Test2", "Pa123", "mail.m@mail.com")
addUserToCSV("userdb", "Test3", "Passord123", "mail44@mail.com")
addUserToCSV("userdb", "geir", "passord", "mail@mail.com")
addUserToCSV("userdb", "gEiR2", "Passord1234", "m.a.i.l.2@mail.com")
addUserToCSV("userdb", "geir3", "Passord1234", "mini_mail.mail@com")
addUserToCSV("userdb", "geir69", "Passord1234", "mail.mail@..com")
addUserToCSV("userdb", "geir69", "Passord1234", "mail.mail@.com")



readCSV("userdb")
"""