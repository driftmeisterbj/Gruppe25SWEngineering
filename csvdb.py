import csv

def resetCSV(filename):
    with open(filename+".csv", "w", newline="") as file:
        writer = csv.DictWriter(file, ["username", "password", "email"])
        writer.writeheader()


def isUsernameTaken(username, filename):
    listOfUsernames = []
    with open(filename+".csv", "r") as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            listOfUsernames.append(line[0])

    if username.lower() in listOfUsernames:
        return True
    else:
        return False

def isUsernameValid(username):
    isValid = True
    illegalChars=["'", '"', ",", "!", "@", "$", "€", "{", "}",
                 "[", "]", "(", ")", "^", "¨", "~", "*", ".",
                 "&", "%", "¤", "#", "!", "?", "+", " "]
    
    if len(username) < 3:
        isValid = False
        print(f'Name: "{username}" failed - Username can not be shorter than 3 characters')

    elif len(username) > 25:
        isValid = False
        print(f'Name: "{username}" failed - Username can not be longer than 25 characters')

    else:
        for char in username:
            if char in illegalChars:
                isValid = False
                print(f'Username contains illegal character: " {char} "')

    return isValid

def isPasswordValid(password):
    isValid = False   
    containsUppercase = False
    containsLowercase = False
    containsNumber = False

    if len(password) < 4:
        print("Password cannot be shorter than 4 characters")

    elif len(password) > 45:
        print("Password cannot be longer than 45 characters")

    else:
        for char in password:
            if char.isupper():
                containsUppercase = True
            if char.islower():
                containsLowercase = True
            if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                containsNumber = True
    
    if (containsUppercase and containsLowercase and containsNumber):
        isValid = True

    return isValid

def isEmailTaken(email, filename):
    listOfEmails = []
    with open(filename+".csv", "r") as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            listOfEmails.append(line[2])

    if email.lower() in listOfEmails:
        return True
    else:
        return False
    
def isEmailValid(email):
    isValid = False
    containsAt = False
    containsPunctuation = False
    containsNoDuplicates = False
    containsOnlyLegalChars = True

    illegalChars=["'", '"', ",", "!", "$", "€", "{", "}",
                 "[", "]", "(", ")", "^", "¨", "~", "*",
                 "&", "%", "¤", "#", "!", "?", "+", " "]

    dupeDict = {}

    for char in email:  
        if char in illegalChars:
            containsOnlyLegalChars = False
            print(f'ERROR - Illegal character " {char} " in email adress')
        if char not in dupeDict.keys():
            dupeDict[char] = 1
        else:
            dupeDict[char] += 1
        

    if "@" in dupeDict.keys():
        containsAt = True
        if dupeDict["@"] == 1:
            if "." in dupeDict.keys():
                containsPunctuation = True
                containsNoDuplicates = True
            else:
                print('Email MUST contain the character " . "')

        else:
            print('Email contains too many instances of the char " @ ", you can only use this character ONCE')
    else:
        print('Email MUST contain the character " @ "')
    
    if containsAt and containsPunctuation and containsNoDuplicates and containsOnlyLegalChars:
        punctuationLastIndex = 0
        counter = 0
        
        for char in email:
            if char == ".":
                punctuationLastIndex = counter    
            counter += 1


        if punctuationLastIndex < email.index("@"):
            print('ERROR - The character MUST appear at least once after the character " @ " in the email adress')
        else:
            isValid = True

    return isValid

    
    

def addUserToCSV(filename, username, password, email):
    if isUsernameValid(username):
        if isUsernameTaken(username, filename) == False:
                if isPasswordValid(password):
                    if isEmailValid(email):
                        if isEmailTaken(email, filename) == False:
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


resetCSV("userdb")
addUserToCSV("userdb", "Test1", "Passord123", "ma!i?l@mail.com")
addUserToCSV("userdb", "Test2", "Pa123", "mail.m@mail.com")
addUserToCSV("userdb", "Test3", "Passord123", "mail44@mail.com")
addUserToCSV("userdb", "geir", "passord", "mail@mail.com")
addUserToCSV("userdb", "gEiR2", "Passord1234", "m.a.i.l.2@mail.com")
addUserToCSV("userdb", "geir3", "Passord1234", "mini_mail.mail@com")



readCSV("userdb")