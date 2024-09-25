import csv

def resetCSV(filename):
    with open(filename+".csv", "w", newline="") as file:
        writer = csv.DictWriter(file, ["username", "password"])
        writer.writeheader()

#resetCSV("userdb")

def addUserToCSV(username, password):
    with open("userdb.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, ["username", "password"])
        writer.writerows([{"username": username, "password": password}])

#addUserToCSV("arne", "passord123")
#addUserToCSV("user2", "69")
#addUserToCSV("1", "2")

def readCSV(filename):
    with open(filename+".csv", "r") as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            print(line)

readCSV("userdb")