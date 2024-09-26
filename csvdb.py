import csv

def resetCSV(filename):
    with open(filename+".csv", "w", newline="") as file:
        writer = csv.DictWriter(file, ["username", "password"])
        writer.writeheader()

#resetCSV("userdb")

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


def addUserToCSV(filename, username, password):
    if isUsernameTaken(username, filename) == False:
         with open(filename+".csv", "a", newline="") as file:
            writer = csv.DictWriter(file, ["username", "password"])
            writer.writerows([{"username": username, "password": password}])
    else:
        print("Username is already taken")

addUserToCSV("userdb", "arne", "passord123")
#addUserToCSV("userdb", "user2", "69")
#addUserToCSV("userdb", "1", "2")

def readCSV(filename):
    with open(filename+".csv", "r") as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            print(line)



readCSV("userdb")