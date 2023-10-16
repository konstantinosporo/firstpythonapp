import pickle
# Desiriaze objects from file for reading the file
def desirializeUserList():
    with open("db/userList.pkl", "rb") as inFile:
        try:
            while True:
                user = pickle.load(inFile)
                print("User ID:", user.userID)
                print("Username:", user.username)
                print("Password:", user.password)
        except EOFError:
            pass
