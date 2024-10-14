import json

# Nullstiller hele JSON-filen, altså full reset.
# Kan fjernes i fremtiden.
def reset_json(filename):
    with open(filename+".json", "w", newline="") as file:
        json.dump({}, file)

# Leser ut innholdet på JSON-filen. Dersom filen ikke finnes returneres en tom liste.
# Dersom noe annet skjer som gjør at den feiler, vil programmet crashe.
def read_json(filename):
    try:
        with open(filename+".json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Itererer gjennom alle brukernavnene til de ulike brukerne på filen og sjekker om det gitte brukernavnet
# allerede eksisterer. Returnerer True hvis brukernavnet eksisterer, False hvis ikke.
def is_username_taken(username, filename):
    users = read_json(filename)

    for user in users:
        for key, value in user.items():
            if key == "username" and value == username.lower():
                return True
    
    return False
                
# Sjekker stringen til brukernavn for å passe på at det er gyldig.
# Returnerer True hvis gyldig, hvis ikke returneres en feilmelding (string).
def is_username_valid(username):
    illegal_chars=["'", '"', ",", "!", "@", "$", "€", "{", "}",
                 "[", "]", "(", ")", "^", "¨", "~", "*", ".",
                 "&", "%", "¤", "#", "!", "?", "+", " "]
    
    if len(username) < 3:
        return f'Name: "{username}" failed - Username can not be shorter than 3 characters'

    elif len(username) > 25:
        return f'Name: "{username}" failed - Username can not be longer than 25 characters'

    else:
        for char in username:
            if char in illegal_chars:
                return f'Username contains illegal character: " {char} "'

    return True

# Sjekker om passordet er gyldig. Dersom passordet er gyldig returneres True.
# Dersom passordet ikke er gyldig returneres en feilmelding.
def is_password_valid(password):
    is_valid = False   
    contains_uppercase = False
    contains_lowercase = False
    contains_number = False

    if len(password) < 4:
        return "Password cannot be shorter than 4 characters"

    elif len(password) > 45:
        return "Password cannot be longer than 45 characters"

    else:
        for char in password:
            if char.isupper():
                contains_uppercase = True
            if char.islower():
                contains_lowercase = True
            if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                contains_number = True
    
    if (contains_number == False):
        return "Password must contain at least one number"

    if (contains_uppercase and contains_lowercase and contains_number):
        is_valid = True

    return is_valid

# Itererer gjennom alle epostene til de ulike brukerene i databasen.
# Dersom eposten er lik en av disse returneres True. Dersom ikke, returneres False
def is_email_taken(email, filename):
    users = read_json(filename)

    for user in users:
        for key, value in user.items():
            if key == "email" and value == email.lower():
                return True
    
    return False

 
def is_email_valid(email):
    is_valid = False
    contains_at = False
    contains_punctuation = False
    contains_no_duplicates = False
    contains_only_legal_chars = True

    illegal_chars=["'", '"', ",", "!", "$", "€", "{", "}",
                 "[", "]", "(", ")", "^", "¨", "~", "*",
                 "&", "%", "¤", "#", "!", "?", "+", " "]
    
    for char in email:  
        if char in illegal_chars:
            contains_only_legal_chars = False
            return f'ERROR - Illegal character " {char} " in email adress'
           
    contains_punctuation = True
    contains_no_duplicates = True
    if email.count("@") > 0:
        contains_at = True
        if email.count("@") == 1:
            if email.count(".") > 0:
                contains_punctuation = True
                contains_no_duplicates = True
            else:
                return 'Email MUST contain the character " . "'
        else:
            return 'Email contains too many instances of the char " @ ", you can only use this character ONCE'
    else:
        return 'Email MUST contain the character " @ "'

    if contains_at and contains_punctuation and contains_no_duplicates and contains_only_legal_chars:
        charList = []
        for char in range(email.index("@"), len(email)):
            charList.append(email[char])

        print(charList)
        if charList.count(".") > 1:
            return 'ERROR - There can only be a single instance of the character " . " after the " @ "'
        
        else:
            punctuation_last_index = 0
            counter = 0
            
            for char in email:
                if char == ".":
                    punctuation_last_index = counter    
                counter += 1

            if punctuation_last_index < email.index("@"):
                return 'ERROR - The character " . " MUST appear at least once after the character " @ " in the email adress'
            else:
                return True

    
    

def add_user_to_json(filename, username, password, email):
    if is_username_valid(username) == True:
        if is_username_taken(username, filename) == False:
            if is_password_valid(password) == True:
                if is_email_valid(email) == True:
                    if is_email_taken(email, filename) == False:
                            users = read_json(filename)
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


def is_device_valid(device):
    required_keys = ['prod_id','name','brand','category']
    for key in required_keys:
        if key not in device:
            return False
    return True

def find_user_index(filename, username):
    users = read_json(filename)
    
    counter = 0
    for user in users:
        if user.get("username").lower() == username.lower():
            return counter
        counter+=1

    return -1


def add_device_to_user(filename, username, device):
    user_index = find_user_index(filename, username)

    if not is_device_valid(device):
        return 'Device invalid'

    if user_index != -1:
        users = read_json(filename)
        user = users[user_index]
        device_list = user["devices"]
        device_list.append(device)

        #Ny: Checks if the device exists already
        device_exists = any(d['prod_id'] == device['prod_id'] for d in device_list)
        if not device_exists:
            device_list.append(device)
        else:
            print('device already added')

        with open(filename+".json", "w") as file:
            data = {
                "username": user["username"],
                "password": user["password"],
                "email": user["email"],
                "devices": device_list
            }

            user = data
            json.dump(users, file, indent=4)

    else:
        print("user_index not found")


def find_device_list_user(filename, username):
    user_index = find_user_index(filename, username)
    
    if user_index != -1:
        users = read_json(filename)
        user = users[user_index]
        device_list = user["devices"]
        return device_list

    else:
        print("user_index not found")

def remove_duplicate_devices_from_user(filename, username):
    user_index = find_user_index(filename, username)

    if user_index == -1:
        print("user_index not found")

    else:
        users = read_json(filename)
        devices = find_device_list_user("userdb", username)

        #https://stackoverflow.com/questions/9427163/remove-duplicate-dict-in-list-in-python
        noDupes = set()
        new_list = []

        for device in devices:
            t = tuple(device.items())
            if t not in noDupes:
                noDupes.add(t)
                new_list.append(device)

        users[user_index]["devices"] = new_list

        with open(filename+".json", "w") as file:
            json.dump(users, file, indent=4)


def create_new_device(name, brand, device_type):
    print()

""""
dev1 = {
    "name": "Vaskemaskin",
    "brand": "Miele"
}
add_device_to_user("userdb", "Test3", dev1)
#reset_json("userdb")

add_user_to_json("userdb", "Test1", "Passord123", "ma!i?l@mail.com")
add_user_to_json("userdb", "Test2", "Pa123", "mail.m@mail.com")
add_user_to_json("userdb", "Test3", "Passord123", "mail44@mail.com")
add_user_to_json("userdb", "geir", "passord", "mail@mail.com")
add_user_to_json("userdb", "gEiR2", "Passord1234", "m.a.i.l.2@mail.com")
add_user_to_json("userdb", "geir3", "Passord1234", "mini_mail.mail@com")
add_user_to_json("userdb", "geir69", "Passord1234", "mail.mail@..com")
add_user_to_json("userdb", "geir69", "Passord1234", "mail.mail@.com")
"""