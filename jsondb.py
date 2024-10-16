import json

# Skriver til JSON-filen med tomt innhold, altså full reset.
# KUN for testing, kan fjernes når vi har ferdigstilt struktur i databasen.
# Mangler feilhåndering
def reset_json(filename):
    with open(filename+".json", "w", newline="") as file:
        json.dump({}, file)

# Åpner json-filen for lesing og returnerer innholdet i en liste.
# Dersom en feil skjer ved lesing, returneres en tom liste
def read_json(filename):
    try:
        with open(filename+".json", "r") as file:
            return json.load(file)

    except:
        return []

# Databasen leses ved bruk av read_json() og denne listen gås gjennom.
# Dersom brukernavnet eksisterer i databasen allerede returneres True, ellers returneres False
def is_username_taken(username, filename):
    users = read_json(filename)

    for user in users:
        for key, value in user.items():
            if key == "username" and value == username.lower():
                return True
    
    return False
                
# Funksjonen kjører en rekke med sjekker på stringen "username" for validering av brukernavn.
# Dersom brukernavnet går gjennom alle sjekkene er brukernavnet gyldig, og funksjonen returnerer True.
# Dersom brukernavnet feiler på en av sjekkene returneres en string med feilmelding.
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


# Funksjonen kjører en rekke med sjekker på stringen "password" for validering av passord.
# Dersom passordet går gjennom alle sjekkene returneres True, ellers returneres en feilmelding
def is_password_valid(password):  
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
    
    if(contains_uppercase == False):
        return "Password must contain at least one uppercase letter"

    if(contains_lowercase == False):
        return "Password must contain at least one lowercase letter"

    if (contains_number == False):
        return "Password must contain at least one number"


    return True

# Henter ut innholdet i databasen og sjekker om eposten eksisterer her allerede.
# Dersom eposten eksisterer er eposten i bruk, og True returneres. Ellers returneres False.
def is_email_taken(email, filename):
    users = read_json(filename)

    for user in users:
        for key, value in user.items():
            if key == "email" and value == email.lower():
                return True
    
    return False
    
# Funksjon for validering av epost. Inneholder en rekke sjekker for at e-post skal være gyldig til bruk.
# Dersom eposten går gjennom alle sjekkene er den gyldig, og True returneres. Ellers returneres en string med feilmelding.
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

    
    
# Funksjon for å legge til en ny bruker i databasen.
# Hvis alle sjekkene går gjennom skrives denne brukeren inn til databasen.
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

# Funksjon for validering av en enhet.
# Sjekker at alle nøklene stemmer med hva en enhet skal inneholde.
# Hvis enheten inneholder alle nøklene returneres True. Ellers returneres Falses
def is_device_valid(device):
    required_keys = ['prod_id','name','brand','category']
    for key in required_keys:
        if key not in device:
            return False
    return True

# Denne funksjonen finder hvilken index, altså plass i listen, en bruker ligger på.
# Hvis brukeren blir funnet returneres indexen. Ellers returneres -1
def find_user_index(filename, username):
    users = read_json(filename)
    
    counter = 0
    for user in users:
        if user.get("username").lower() == username.lower():
            return counter
        counter+=1

    return -1

# Denne funksjonen legger til en enhet i listen til en bruker, og skriver denne endringen til databasen.
def add_device_to_user(filename, username, device):
    user_index = find_user_index(filename, username)

    if not is_device_valid(device):
        return 'Device invalid'

    if user_index != -1:
        users = read_json(filename)
        user = users[user_index]
        device_list = user["devices"]
        device_list.append(device)

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
        no_dupes = set()
        new_list = []

        for device in devices:
            t = tuple(device.items())
            if t not in no_dupes:
                no_dupes.add(t)
                new_list.append(device)

        users[user_index]["devices"] = new_list

        with open(filename+".json", "w") as file:
            json.dump(users, file, indent=4)

# Oprette nytt device
def create_new_device(name, brand, device_type):
    print()

# Slette et device fra en bruker
def delete_device_from_user():
    print()

# Endre på dataen til et device fra bruker sin device-liste
def modify_device_information():
    print()


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
add_device_to_user("userdb", "Test3", dev2)
add_device_to_user("userdb", "Test3", dev3)
add_device_to_user("userdb", "Test3", dev4)

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