import csv

def resetCSV(filename):
    with open(filename+".csv", "w", newline="") as file:
        writer = csv.DictWriter(file, ["username", "password"])
        writer.writeheader()


def isUsernameTaken(username, filename):
    listOfUsernames = []
    with open(filename+".csv", "r") as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            listOfUsernames.append(line[0])

    if username in listOfUsernames:
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
    isValid = True   
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
    
    else:
        isValid = False

    return isValid


def addUserToCSV(filename, username, password):
    if isUsernameTaken(username, filename) == False:
        if isUsernameValid(username):
            if isPasswordValid(password):
                with open(filename+".csv", "a", newline="") as file:
                    writer = csv.DictWriter(file, ["username", "password"])
                    writer.writerows([{"username": username.lower(), "password": password}])
            else:
                print("Password is invalid - Password must contain an uppercase letter, a lowercase letter and a number")
        else:
            print("Username is invalid. Check error messages in console.")
    else:
        print("Username is already taken")


def readCSV(filename):
    with open(filename+".csv", "r") as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            print(line)


resetCSV("userdb")
addUserToCSV("userdb", "Arne", "Passord123")
addUserToCSV("userdb", "user2", "69")
addUserToCSV("userdb", "1", "2")
print(isUsernameValid("arne'2"))

readCSV("userdb")