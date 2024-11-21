import json
from abc import ABC,abstractmethod
import os
import sys
path = os.path.join(os.path.dirname(__file__), "devices")
sys.path.append(path)
from devices import fridge, heater, lock, light, camera, device_class
from dbinterface import DatabaseInterface


class ReadWrite(ABC):
    @abstractmethod
    def read(self, fileName):
        pass
    @abstractmethod
    def write(self, fileName, text):
        pass
    @abstractmethod
    def reset(self, fileName):
        pass
class JsonReadWrite(ReadWrite):
    @staticmethod
    def read(fileName):
        try:
            with open(fileName, "r") as file:
                return json.load(file)
        except:
            return []

    @staticmethod
    def write(fileName, data):

        try:
            with open(fileName, "w") as file:
                json.dump(data,file, indent=4)
            return True
        except:
            pass
        return False

    @staticmethod
    def reset(fileName):
        try:
            with open(fileName, "w") as file:
                file.write("{}")
            return True
        except:
            pass
        return False

class JsonDatabase(DatabaseInterface):
    def __init__(self, filename) -> None:
        self.filename = filename + ".json"
        self.data = self.read_database()
        JsonReadWrite.write(self.filename, self.data)

    # Skriver til JSON-filen med tomt innhold, altså full reset.
    # KUN for testing, kan fjernes når vi har ferdigstilt struktur i databasen.
    # Returnerer True hvis databasen resettes, False hvis ikke
    def reset_database(self):
        try:
            with open(self.filename, "w") as file:
                file.write("{}")
            return True
        except:
            return False
        
    # Åpner json-filen for lesing og returnerer innholdet i en liste.
    # Dersom en feil skjer ved lesing, returneres en tom liste
    def read_database(self):
        return JsonReadWrite.read(self.filename)

    # Databasen leses ved bruk av read_database() og denne listen gås gjennom.
    # Dersom brukernavnet eksisterer i databasen allerede returneres True, ellers returneres False
    """
    --- Parametere ----
    username - String
    """
    def is_username_taken(self, username):
        users = self.read_database()

        for user in users:
            for key, value in user.items():
                if key == "username" and value.lower() == username.lower():
                    return True

        return False

    # Funksjonen kjører en rekke med sjekker på stringen "username" for validering av brukernavn.
    # Dersom brukernavnet går gjennom alle sjekkene er brukernavnet gyldig, og metoden returnerer True.
    # Dersom brukernavnet feiler på en av sjekkene returneres en string med feilmelding.
    """
    --- Parametere ----
    username - String
    """
    def is_username_valid(self, username):
        illegal_chars=["'", '"', ",", "!", "@", "$", "€", "{", "}",
                    "[", "]", "(", ")", "^", "¨", "~", "*", ".",
                    "&", "%", "¤", "#", "!", "?", "+", " ", ";", ":"]

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
    """
    --- Parametere ----
    password - String
    """
    def is_password_valid(self, password):  
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
    """
    --- Parametere ----
    email - String
    """
    def is_email_taken(self, email):
        users = self.read_database()

        for user in users:
            for key, value in user.items():
                if key == "email" and value.lower() == email.lower():
                    return True

        return False

    # Funksjon for validering av epost. Inneholder en rekke sjekker for at e-post skal være gyldig til bruk.
    # Dersom eposten går gjennom alle sjekkene er den gyldig, og True returneres. Ellers returneres en string med feilmelding.
    """
    --- Parametere ----
    email - String
    """
    def is_email_valid(self, email):
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
    """
    --- Parametere ----
    username - String
    password - String
    email - String
    """
    def add_user_to_database(self, username, password, email):
        if self.is_username_valid(username) != True:
            return "Username is invalid. Check error messages in console."
        
        if self.is_username_taken(username) != False:
            return "Username is already taken"

        if self.is_password_valid(password) != True:
            return "Password is invalid - Password must contain an uppercase letter, a lowercase letter and a number"
        
        if self.is_email_valid(email) != True:
            return "Email is invalid. Check error messages in console."
                 
        if self.is_email_taken(email) != False:
            return "An account with this email adress already exists"
        
        data = self.read_database()
        new_data = {
            "username": username,
            "password": password,
            "email": email,
            "devices": []
        }
        data.append(new_data)
        JsonReadWrite.write(self.filename, data)

        return True

    # Funksjon for validering av en enhet.
    # Sjekker at alle nøklene stemmer med hva en enhet skal inneholde.
    # Hvis enheten inneholder alle nøklene returneres True. Ellers returneres Falses
    """
    --- Parametere ----
    device - Objekt av klassen "Device"
    """
    def is_device_valid(self, device):
        device_dict = device.get_dict()
        required_keys = ['prod_id','name','brand','category']
        for key in required_keys:
            if key not in device_dict:
                return False
        return True



    # Denne metoden finder hvilken index, altså plass i listen, en bruker ligger på.
    # Hvis brukeren blir funnet returneres indexen. Ellers returneres -1
    """
    --- Parametere ----
    username - String
    """
    def find_user_index(self, username):
        data = self.read_database()

        counter = 0
        for user in data:
            if user.get("username").lower() == username.lower():
                return counter
            counter+=1

        return -1

    # Denne metoden legger til en enhet i listen til en bruker, og skriver denne endringen til databasen.
    # Returnerer True hvis alt går bra, False hvis brukeren ikke finnes, String med feilmelding desom noe annet skjer.
    """
    --- Parametere ----
    username - String
    device - Objekt av klassen "Device"
    """
    def add_device_to_user(self, username, device):
        user_index = self.find_user_index(username)

        if not self.is_device_valid(device):
            return 'Device invalid'

        if user_index != -1:
            users = self.read_database()
            user = users[user_index]
            device_list = user["devices"]
            device_data = device.get_dict()

            device_exists = any(d['prod_id'] == device_data["prod_id"] for d in device_list)
            if not device_exists:
                device_list.append(device_data)
            else:
                return 'Device already added'

            data = {
                "username": user["username"],
                "password": user["password"],
                "email": user["email"],
                "devices": device_list
            }

            user = data
            users[user_index] = user
            
            JsonReadWrite.write(self.filename, users)
            return True
        else:
            return False

    # Returnerer listen med enheter til en bruker.
    # Dersom brukeren ikke finnes returneres en tom liste.
    """
    --- Parametere ----
    username - String
    """
    def find_device_list_user(self, username):
        user_index = self.find_user_index(username)

        if user_index != -1:
            users = self.read_database()
            user = users[user_index]
            device_list = user["devices"]
            return device_list

        else:
            return []

    # Denne metoden eksisterer for å fjerne eventuelle duplikater i en enhetsliste.
    # Det finnes andre sjekker på plass. Denne metoden ble laget før det eksisterte andre sikkerhetsnett.
    # Men den brukes fortsatt i tilfelle noe skulle. Returnerer False dersom en bruker ikke finnes, 
    # True dersom metoden kjører ferdig.
    """
    --- Parametere ----
    username - String
    """
    def remove_duplicate_devices_from_user(self, username):
        user_index = self.find_user_index(username)

        if user_index == -1:
            return False

        else:
            data = self.read_database()
            devices = self.find_device_list_user(username)

            #https://stackoverflow.com/questions/9427163/remove-duplicate-dict-in-list-in-python
            no_dupes = set()
            new_list = []

            for device in devices:
                t = tuple(device.items())
                if t not in no_dupes:
                    no_dupes.add(t)
                    new_list.append(device)

            data[user_index]["devices"] = new_list

            JsonReadWrite.write(self.filename, data)
            return True

    # Metode for å opprette et objekt. Bruker kategori for å lage de ulike objektene.
    # Returnerer objektet, returnerer False dersom funksjonaliteten for kategorien ikke er implementert.
    """
    --- Parametere ----
    prod_id - int
    name - String
    brand - String
    category - String
    """
    def create_new_device(self, prod_id, name, brand, category):
        if category == "Fridge":
            return fridge.Fridge(prod_id, name, brand)
        
        if category == "Lock":
            return lock.Lock(prod_id, name, brand)

        if category == "Camera":
            return camera.Camera(prod_id, name, brand)
        
        if category == "Heater":
            return heater.Heater(prod_id, name, brand)
        
        if category == "Light":
            return light.Light(prod_id, name, brand)
        
        return False

    # Denne metoden brukes for å slette en enhet fra en bruker.
    # Hvis brukeren ikke finnes returneres False. Hvis sletting av enheten ikke funker, 
    # f.eks. ved at enheten ikke eksisterer, returneres en feilmelding.
    # Returnerer True dersom fjerningen funket.
    """
    --- Parametere ----
    username - String
    device - Objekt av klassen "Device"
    """
    def delete_device_from_user(self, username, device):
        user_index = self.find_user_index(username)

        if user_index != -1:
            users = self.read_database()
            user = users[user_index]
            device_list = user["devices"]

            device_dict = device.get_dict()

            try:
                device_list.remove(device_dict)
            except:
                return "Device could not be found"
            
            data = {
                "username": user["username"],
                "password": user["password"],
                "email": user["email"],
                "devices": device_list
            }

            user = data
            users[user_index] = user
            JsonReadWrite.write(self.filename, users)
            return True

        else:
            return False
            
    # Hver gang det leses fra json blir enhetene omgjort fra objekter til dictionaries
    # Metoden tar dictionary-en til en enhet og returnerer det som et objekt.
    # Dersom kategorien er ukjent returneres False.
    """
    --- Parametere ----
    device_dict - Dictionary
    """
    def recreate_object(self, device_dict):
        category = device_dict['category']

        if category == 'Light':
            return light.Light(
            prod_id=device_dict["prod_id"],
            name=device_dict["name"],
            brand=device_dict["brand"],
            on=device_dict["on"],
            brightness=device_dict.get("brightness", 100)
            )
        elif category == 'Fridge':
            return fridge.Fridge(
            prod_id=device_dict["prod_id"],
            name=device_dict["name"],
            brand=device_dict["brand"],
            on=device_dict["on"],
            temperature=device_dict.get("temperature", 15)
            )
        elif category == "Heater":
            return heater.Heater(
            prod_id=device_dict["prod_id"],
            name=device_dict["name"],
            brand=device_dict["brand"],
            on=device_dict["on"],
            temperature=device_dict.get("temperature", 15)
            )
        elif category == "Lock":
            return lock.Lock(
            prod_id=device_dict["prod_id"],
            name=device_dict["name"],
            brand=device_dict["brand"],
            on=device_dict["on"],
            entry_code=device_dict.get("entry_code", "1234")
            )
        elif category == "Camera":
            return camera.Camera(
            prod_id=device_dict["prod_id"],
            name=device_dict["name"],
            brand=device_dict["brand"],
            on=device_dict["on"],
            resolution=device_dict.get("resolution", "1080p"),
            status=device_dict.get("status", "Inactive"),
            motion_detection=device_dict.get("motion_detection", False)
            )
        else:
            return False


    # Denne metoden oppdaterer data for en enhet i brukeren sin enhetsliste.
    # Metoden vil oppdatere informasjonen til enheten som har lik "prod_id" som enheten gitt som parameter.
    # Det er viktig at "device" her refererer til et objekt, ikke dictionary.
    """
    --- Parametere ----
    username - String
    device - Objekt av klassen "Device"
    """
    def update_device_data(self,username, device):
        user_index = self.find_user_index(username)

        users = self.read_database()
        user = users[user_index]
        device_list = user['devices']

        for i, user_device in enumerate(device_list):
            if user_device['prod_id'] == device.prod_id:
                user_device["name"] = device.name
                user_device["brand"] = device.brand
                user_device["category"] = device.category
                user_device["on"] = device.on

                if device.category == "Fridge" or device.category == "Heater":
                    user_device["temperature"] = device.temperature
                elif device.category == "Light":
                    user_device["brightness"] = device.brightness
                elif device.category == "Lock":
                    user_device["status"] = device.status
                    user_device["entry_code"] = device.entry_code
                elif device.category == "Camera":
                    user_device["resolution"] = device.resolution
                    user_device["status"] = device.status
                    user_device["motion_detection"] = device.motion_detection
                
                JsonReadWrite.write(self.filename, users)


    # Finner en bruker i databasen og returnerer et dictionary
    # for denne brukeren. Hvis brukeren ikke blir funnet blir et tomt dictionary returnert.
    """
    --- Parametere ----
    username - String
    """
    def get_current_user(self, username):
        user_index = self.find_user_index(username)
        if user_index != -1:
            users = self.read_database()
            user = users[user_index]
            return {
                'username':user['username'],
                'email':user['email'],
                'devices':user['devices']
            }


        else:
            return {
                'username': None,
                'email': None,
                'devices': []
            }


    