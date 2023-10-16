import pickle


class User():
    userID = None
    username = ""
    password = ""

    def __init__(self, userID, username, password):
        self.userID = userID
        self.username = username
        self.password = password

# New user object creation


def createNewUser():
    userID = str(input("Enter userID:"))
    username = input("Enter username:")
    password = input("Enter password:")

    newUser = User(userID, username, password)

    with open("db/userList.pkl", "ab") as outFile:
        pickle.dump(newUser, outFile)

 
