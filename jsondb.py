import json

def resetJSON(filename):
    with open(filename+".json", "w", newline="") as file:
        json.dump({}, file)

def readJSON(filename):
    try:
        with open(filename+".json", "r") as file:
            return json.load(file)

    except:
        return []


def isUsernameTaken(username, filename):
    users = readJSON(filename)

    for user in users:
        for key, value in user.items():
            if key == "username" and value == username.lower():
                return True
    
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
    users = readJSON(filename)

    for user in users:
        for key, value in user.items():
            if key == "email" and value == email.lower():
                return True
    
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
    
    for char in email:  
        if char in illegalChars:
            containsOnlyLegalChars = False
            print(f'ERROR - Illegal character " {char} " in email adress')
           
    containsPunctuation = True
    containsNoDuplicates = True
    if email.count("@") > 0:
        containsAt = True
        if email.count("@") == 1:
            if email.count(".") > 0:
                containsPunctuation = True
                containsNoDuplicates = True
            else:
                print('Email MUST contain the character " . "')
        else:
            print('Email contains too many instances of the char " @ ", you can only use this character ONCE')
    else:
        print('Email MUST contain the character " @ "')

    if containsAt and containsPunctuation and containsNoDuplicates and containsOnlyLegalChars:
        charList = []
        for char in range(email.index("@"), len(email)):
            charList.append(email[char])

        print(charList)
        if charList.count(".") > 1:
            print('ERROR - There can only be a single instance of the character " . " after the " @ "')
        
        else:
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

    
    

def addUserToJSON(filename, username, password, email):
    if isUsernameValid(username):
        if isUsernameTaken(username, filename) == False:
                if isPasswordValid(password):
                    if isEmailValid(email):
                        if isEmailTaken(email, filename) == False:
                                users = readJSON(filename)
                                with open(filename+".json", "w") as file:
                                    data = {
                                        "username": username,
                                        "password": password,
                                        "email": email,
                                        "devices": []
                                    }
                                    users.append(data)
                                    json.dump(users, file, indent=4)
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


def findUserIndex(filename, username):
    users = readJSON(filename)
    
    counter = 0
    for user in users:
        if user.get("username").lower() == username.lower():
            return counter
        counter+=1

    return -1

#Check if device is valid
def isDeviceValid(device):
    required_keys = ['prod_id','name','brand','category']
    for key in required_keys:
        if key not in device:
            return False
    return True

def addDeviceToUser(filename, username, device):
    if not isDeviceValid(device):
        print('Device invalid')
        return


    userIndex = findUserIndex(filename, username)

    if userIndex != -1:
        users = readJSON(filename)
        user = users[userIndex]
        deviceList = user["devices"]

        #Checks if the device exists already
        device_exists = any(d['prod_id'] == device['prod_id'] for d in deviceList)
        if not device_exists:
            deviceList.append(device)
        else:
            print('device already added')

        with open(filename+".json", "w") as file:
            data = {
                "username": user["username"],
                "password": user["password"],
                "email": user["email"],
                "devices": deviceList
            }

            user = data
            json.dump(users, file, indent=4)

    else:
        print("Userindex not found")

dev1 = {
    "name": "Vaskemaskin",
    "brand": "Miele"
}
dev2 = {
    "name":"Hue",
    "brand":"phillips",
    "category":'light'
}
dev3 = {
    "name":"Hue",
    "brand":"phillips",
    "category":'light'
}
dev4 = {
    "prod_id":'11564',
    "name":"Hue 2.0",
    "brand":"phillips",
    "category":'light'
}
addDeviceToUser("userdb", "Test3", dev2)
addDeviceToUser("userdb", "Test3", dev3)
addDeviceToUser("userdb", "Test3", dev4)

#resetJSON("userdb")

# addUserToJSON("userdb", "Test1", "Passord123", "ma!i?l@mail.com")

# addUserToJSON("userdb", "Test2", "Pa123", "mail.m@mail.com")
# addUserToJSON("userdb", "Test3", "Passord123", "mail44@mail.com")
# addUserToJSON("userdb", "geir", "passord", "mail@mail.com")
# addUserToJSON("userdb", "gEiR2", "Passord1234", "m.a.i.l.2@mail.com")
# addUserToJSON("userdb", "geir3", "Passord1234", "mini_mail.mail@com")
# addUserToJSON("userdb", "geir69", "Passord1234", "mail.mail@..com")
# addUserToJSON("userdb", "geir69", "Passord1234", "mail.mail@.com")
# addDeviceToUser("userdb","Test3",)